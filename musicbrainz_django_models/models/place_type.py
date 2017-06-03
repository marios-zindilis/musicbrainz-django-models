"""
.. module:: place_type

The **Place Type** Model.

PostgreSQL Definition
---------------------

The :code:`place_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place_type ( -- replicate
        id                  SERIAL, -- PK
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references place_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


def pre_save_place_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICES_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError('Place Type "{}" is not one of: {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICES_LIST)))


@python_2_unicode_compatible
class place_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: The name can have one of a few values, not restricted in
        the SQL definition, but picked up from the MusicBrainz Database dump
        of late April 2017. In Django, this is implemented as a `choices`
        parameter to the `name` field, and as a `pre_save` signal that performs
        the validation.
    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    STUDIO = 'Studio'
    VENUE = 'Venue'
    OTHER = 'Other'
    STADIUM = 'Stadium'
    INDOOR_ARENA = 'Indoor Arena'
    RELIGIOUS_BUILDING = 'Religious Building'
    NAME_CHOICES = (
        (STUDIO, STUDIO),
        (VENUE, VENUE),
        (OTHER, OTHER),
        (STADIUM, STADIUM),
        (INDOOR_ARENA, INDOOR_ARENA),
        (RELIGIOUS_BUILDING, RELIGIOUS_BUILDING))
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'place_type'


models.signals.pre_save.connect(pre_save_place_type, sender=place_type)
