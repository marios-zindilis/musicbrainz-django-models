"""
.. module:: artist_alias

PostgreSQL Definition
---------------------

The :code:`artist_alias` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_alias ( -- replicate (verbose)
        id                  SERIAL,
        artist              INTEGER NOT NULL, -- references artist.id
        name                VARCHAR NOT NULL,
        locale              TEXT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        type                INTEGER, -- references artist_alias_type.id
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
        CONSTRAINT search_hints_are_empty
          CHECK (
            (type <> 3) OR ( 
              type = 3 AND sort_name = name AND
              begin_date_year IS NULL AND begin_date_month IS NULL AND begin_date_day IS NULL AND
              end_date_year IS NULL AND end_date_month IS NULL AND end_date_day IS NULL AND
              primary_for_locale IS FALSE AND locale IS NULL 
            )
          )    
    );

"""

from django.db import models


def pre_save_artist_alias(sender, instance, **kwargs):
    instance.ended = instance.check_ended()

    # primary_for_locale cannot be True if locale is empty:
    if instance.locale is None:
        instance.primary_for_locale = False

    from .artist_alias_type import artist_alias_type
    if instance.type == artist_alias_type.SEARCH_HINT:
        instance.sort_name = instance.name
        instance.begin_date_year = None 
        instance.begin_date_month = None 
        instance.begin_date_day = None 
        instance.end_date_year = None 
        instance.end_date_month = None 
        instance.end_date_day = None 
        instance.primary_for_locale = False
        instance.locale = None


class artist_alias(models.Model):
    """ 
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param type: In the PostgreSQL definition of the `artist_alias` table,
        there is a `check` on the `type`, that uses a hardcoded value of `3`.
        The `type` with `id=3` in the `artist_alias_type` table is the
        `Search hint`. If the `type` of the `artist_alias` is `Search hint`,
        then a number of fields are restricted. `sort_name` must be equal to
        `name`. `begin_date_year`, `begin_date_month`, `begin_date_day`,
        `end_date_year`, `end_date_month`, `end_date_day` and `locale` must all
        be empty. `primary_for_locale` must be False. In Django, this is
        implemented in a `pre_save` signal.
    :param str sort_name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param smallint begin_date_month: You'd think this would be validated as a
        range of 1-12 or similar...
    :param smallint end_date_month: ditto
    :param smallint begin_date_day: You'd think this would be validated as a
        range of 1-31 or similar...
    :param smallint end_date_day: ditto
    :param boolean primary_for_locale: The MusicBrainz Server uses a 
        PostgreSQL `check` to validate that this field is False, if the
        `locale` field is empty. In Django, this is implemented with a
        `pre_save` signal.
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        set this to `True` if any of the `end_*` fields has any value. This is
        implemented in Django with a `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey('artist')
    name = models.CharField(max_length=255)
    locale = models.TextField(null=True)
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('artist_alias_type', null=True)
    sort_name = models.CharField(max_length=255)
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    primary_for_locale = models.BooleanField(default=False)
    ended = models.BooleanField(default=False)

    def check_ended(self):
        """
        Set `ended` to `True` if any of the `end_date_*` fields is populated.
        """
        return (
            self.end_date_year is not None or
            self.end_date_month is not None or
            self.end_date_day is not None)

    def __unicode__(self):
        self.name

    def __str__(self):
        self.name

    class Meta:
        db_table = 'artist_alias'


models.signals.pre_save.connect(pre_save_artist_alias, sender=artist_alias)
