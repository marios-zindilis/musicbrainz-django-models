"""
.. module:: abstract__model_alias

This is an Abstract Django Model, meant to be subclassed by Models that store
aliases for other models, namely:

1.  :class:`area_alias`
2.  :class:`artist_alias`
3.  :class:`event_alias`
4.  :class:`instrument_alias`
5.  :class:`label_alias`
6.  :class:`place_alias`
7.  :class:`recording_alias`
8.  :class:`release_alias`
9.  :class:`release_group_alias`
10. :class:`series_alias`
11. :class:`work_alias`

These models are defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_alias ( -- replicate (verbose)
        id                  SERIAL,
        <MODEL>             INTEGER NOT NULL, -- references <MODEL>.id
        name                VARCHAR NOT NULL,
        locale              TEXT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        type                INTEGER, -- references <MODEL>_alias_type.id
        sort_name           VARCHAR NOT NULL,
        begin_date_year     SMALLINT,
        begin_date_month    SMALLINT,
        begin_date_day      SMALLINT,
        end_date_year       SMALLINT,
        end_date_month      SMALLINT,
        end_date_day        SMALLINT,
        primary_for_locale  BOOLEAN NOT NULL DEFAULT false,
        ended               BOOLEAN NOT NULL DEFAULT FALSE
        CHECK (
            (
                -- If any end date fields are not null, then ended must be true
                (end_date_year IS NOT NULL OR
                end_date_month IS NOT NULL OR
                end_date_day IS NOT NULL) AND
                ended = TRUE
            ) OR (
                -- Otherwise, all end date fields must be null
                (end_date_year IS NULL AND
                end_date_month IS NULL AND
                end_date_day IS NULL)
            )
        ),
        CONSTRAINT primary_check CHECK ((locale IS NULL AND primary_for_locale IS FALSE) OR (locale IS NOT NULL)),
    );

Some of those models have an additional constraint, that applies when the
type of the alias is "search hint":

.. code-block:: sql

    CONSTRAINT search_hints_are_empty
    CHECK (
        (type <> 2) OR (
        type = 2 AND sort_name = name AND
        begin_date_year IS NULL AND begin_date_month IS NULL AND begin_date_day IS NULL AND
        end_date_year IS NULL AND end_date_month IS NULL AND end_date_day IS NULL AND
        primary_for_locale IS FALSE AND locale IS NULL
        )
    )

In this case, the `musicbrainz_django_models.signals.pre_save_model_alias`
signal is applied.

"""

from django.db import models


class abstract__model_alias(models.Model):
    """
    When subclassing this abstract model, define:

        <MODEL> = models.ForeignKey(<MODEL>)
        type = models.ForeignKey(<MODEL>_alias_type, null=True)

    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param boolean primary_for_locale: The MusicBrainz Server uses a
        PostgreSQL `check` to validate that this field is False, if the
        `locale` field is empty. In Django, this is implemented by overriding
        `save()`.
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        validate that this is `True` if any of the `end_*` fields has any
        value, and that it is `False` if all the `end_*` fields are empty.
        This could be implemented in a Django model with a `@property` method,
        however that cannot be queried, so it is implemented by overriding
        `save()`.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    locale = models.TextField(null=True)
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    sort_name = models.CharField(max_length=255)
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    primary_for_locale = models.BooleanField(default=False)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # `ended` must be True if any of the end dates are not empty:
        self.ended = (
            self.end_date_year is not None or
            self.end_date_month is not None or
            self.end_date_day is not None)

        # `primary_for_locale` cannot be True if locale is empty:
        if self.locale is None:
            self.primary_for_locale = False

        super(abstract__model_alias, self).save(*args, **kwargs)

    class Meta:
        abstract = True
