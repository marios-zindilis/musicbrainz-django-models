"""
.. module:: event_alias

The **Event Alias** Model.

PostgreSQL Definition
---------------------

The :code:`event_alias` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_alias ( -- replicate (verbose)
        id                  SERIAL,
        event               INTEGER NOT NULL, -- references event.id
        name                VARCHAR NOT NULL,
        locale              TEXT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        type                INTEGER, -- references event_alias_type.id
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
            (type <> 2) OR (
              type = 2 AND sort_name = name AND
              begin_date_year IS NULL AND begin_date_month IS NULL AND begin_date_day IS NULL AND
              end_date_year IS NULL AND end_date_month IS NULL AND end_date_day IS NULL AND
              primary_for_locale IS FALSE AND locale IS NULL
            )
          )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .event_alias_type import event_alias_type


def pre_save_event_alias(sender, instance, **kwargs):
    # `ended` must be True if any of the `end_date_*` fields has a value:
    instance.ended = (
        instance.end_date_year is not None or
        instance.end_date_month is not None or
        instance.end_date_day is not None)

    # `primary_for_locale` cannot be True if `locale` has no value:
    if instance.locale is None:
        instance.primary_for_locale = False

    # if `event_alias` is a search hint, some fields should have specific values:
    if instance.type.name == event_alias_type.SEARCH_HINT:
        instance.sort_name = instance.name
        instance.begin_date_year = None
        instance.begin_date_month = None
        instance.begin_date_day = None
        instance.end_date_year = None
        instance.end_date_month = None
        instance.end_date_day = None
        instance.primary_for_locale = False
        instance.locale = None


@python_2_unicode_compatible
class event_alias(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param event: references :class:`.event`
    """

    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('event')
    name = models.CharField(max_length=255)
    locale = models.TextField(null=True)
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('event_alias_type')
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
        db_table = 'event_alias'


models.signals.pre_save.connect(pre_save_event_alias, sender=event_alias)
