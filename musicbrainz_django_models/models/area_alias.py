"""
.. module:: area_alias

The **Area Alias** Model.

PostgreSQL Definition
---------------------

The :code:`area_alias` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_alias ( -- replicate (verbose)
        id                  SERIAL, --PK
        area                INTEGER NOT NULL, -- references area.id
        name                VARCHAR NOT NULL,
        locale              TEXT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >=0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        type                INTEGER, -- references area_alias_type.id
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
                 CONSTRAINT primary_check
                     CHECK ((locale IS NULL AND primary_for_locale IS FALSE) OR (locale IS NOT NULL)));

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


def pre_save_area_alias(sender, instance, **kwargs):
    # `ended` must be True if any of the end dates is not empty:
    instance.ended = (
        instance.end_date_year is not None or
        instance.end_date_month is not None or
        instance.end_date_day is not None)

    # `primary_for_locale` cannot be True if locale is empty:
    if instance.locale is None:
        instance.primary_for_locale = False


@python_2_unicode_compatible
class area_alias(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param boolean primary_for_locale: The MusicBrainz Server uses a
        PostgreSQL `check` to validate that this field is False, if the
        `locale` field is empty. In Django, this is implemented with a
        `pre_save` signal.
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        validate that this is `True` if any of the `end_*` fields has any
        value, and that it is `False` if all the `end_*` fields are empty.
        This could be implemented in a Django model with a `@property` method,
        however that cannot be queried, so it is implemented here with a
        `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    area = models.ForeignKey('area')
    name = models.CharField(max_length=255)
    locale = models.TextField(null=True)
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('area_alias_type', null=True)
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

    class Meta:
        db_table = 'area_alias'
        verbose_name_plural = 'Area Aliases'


models.signals.pre_save.connect(pre_save_area_alias, sender=area_alias)
