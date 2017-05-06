"""
.. module:: label

The **Label** model.

    See the `Label Documentation on MusicBrainz`_.

.. _Label Documentation on MusicBrainz: https://musicbrainz.org/doc/Label

PostgreSQL Definition
---------------------

The :code:`label` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        begin_date_year     SMALLINT,
        begin_date_month    SMALLINT,
        begin_date_day      SMALLINT,
        end_date_year       SMALLINT,
        end_date_month      SMALLINT,
        end_date_day        SMALLINT,
        label_code          INTEGER CHECK (label_code > 0 AND label_code < 100000),
        type                INTEGER, -- references label_type.id
        area                INTEGER, -- references area.id
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        ended               BOOLEAN NOT NULL DEFAULT FALSE
          CONSTRAINT label_ended_check CHECK (
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
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
import uuid


def pre_save_label(sender, instance, **kwargs):
    instance.ended = instance.check_ended()

    if instance.label_code is not None:
        MIN = sender.LABEL_CODE_MIN
        MAX = sender.LABEL_CODE_MAX
        if not MIN <= instance.label_code <= MAX:
            raise ValidationError(
                'The label_code value is outside the range {} to {}'.format(
                    MIN, MAX))


class label(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param smallint begin_date_month: You'd think this would be validated as a
        range of 1-12 or similar...
    :param smallint end_date_month: ditto
    :param smallint begin_date_day: You'd think this would be validated as a
        range of 1-31 or similar...
    :param smallint end_date_day: ditto
    :param int label_code: The MusicBrainz Server uses a PostgreSQL `check` to
        restrict the values of this fields to 0 < label_code < 100000. In
        Django, this is implemented with validators and with a `pre_save`
        signal.
    :param type: references :class:`.label_type`
    :param area: references :class:`.area`
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        set this to `True` if any of the `end_*` fields has any value. This is
        implemented in Django with a `pre_save` signal.
    """

    LABEL_CODE_MIN = 1
    LABEL_CODE_MAX = 99999

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    label_code = models.PositiveIntegerField(
        null=True,
        validators=[
            MinValueValidator(LABEL_CODE_MIN),
            MaxValueValidator(LABEL_CODE_MAX)])
    type = models.ForeignKey('label_type', null=True)
    area = models.ForeignKey('area', null=True)
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
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
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'label'


models.signals.pre_save.connect(pre_save_label, sender=label)
