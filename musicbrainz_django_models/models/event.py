"""
.. module:: event

The **Event** Model.

PostgreSQL Definition
---------------------

The :code:`event` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        begin_date_year     SMALLINT,
        begin_date_month    SMALLINT,
        begin_date_day      SMALLINT,
        end_date_year       SMALLINT,
        end_date_month      SMALLINT,
        end_date_day        SMALLINT,
        time                TIME WITHOUT TIME ZONE,
        type                INTEGER, -- references event_type.id
        cancelled           BOOLEAN NOT NULL DEFAULT FALSE,
        setlist             TEXT,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        ended               BOOLEAN NOT NULL DEFAULT FALSE
          CONSTRAINT event_ended_check CHECK (
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
          )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


def pre_save_event(sender, instance, **kwargs):
    instance.ended = (
        instance.end_date_year is not None or
        instance.end_date_month is not None or
        instance.end_date_day is not None)


@python_2_unicode_compatible
class event(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param smallint begin_date_month: You'd think this would be validated as a
        range of 1-12 or similar...
    :param smallint end_date_month: ditto
    :param smallint begin_date_day: You'd think this would be validated as a
        range of 1-31 or similar...
    :param smallint end_date_day: ditto
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        validate that this is `True` if any of the `end_*` fields has any
        value, and that it is `False` if all the `end_*` fields are empty.
        This could be implemented in a Django model with a `@property` method,
        however that cannot be queried, so it is implemented here with a
        `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    time = models.TimeField(null=True)
    type = models.ForeignKey('event_type')
    cancelled = models.BooleanField(default=False)
    setlist = models.TextField()
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'event'


models.signals.pre_save.connect(pre_save_event, sender=event)
