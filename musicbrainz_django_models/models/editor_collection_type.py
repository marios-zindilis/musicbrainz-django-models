"""
.. module:: editor_collection_type

The **Editor Collection Type** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_type ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        entity_type         VARCHAR(50) NOT NULL,
        parent              INTEGER, -- references editor_collection_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
import uuid


def pre_save_editor_collection_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICES_LIST:
        raise ValidationError('Name "{}" not in {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICES_LIST)))


@python_2_unicode_compatible
class editor_collection_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    RELEASE = 'Release'
    OWNED_MUSIC = 'Owned music'
    WISHLIST = 'Wishlist'
    EVENT = 'Event'
    ATTENDING = 'Attending'
    MAYBE_ATTENDING = 'Maybe attending'
    AREA = 'Area'
    ARTIST = 'Artist'
    INSTRUMENT = 'Instrument'
    LABEL = 'Label'
    PLACE = 'Place'
    RECORDING = 'Recording'
    RELEASE_GROUP = 'Release group'
    SERIES = 'Series'
    WORK = 'Work'
    NAME_CHOICES = (
        (RELEASE, RELEASE),
        (OWNED_MUSIC, OWNED_MUSIC),
        (WISHLIST, WISHLIST),
        (EVENT, EVENT),
        (ATTENDING, ATTENDING),
        (MAYBE_ATTENDING, MAYBE_ATTENDING),
        (AREA, AREA),
        (ARTIST, ARTIST),
        (INSTRUMENT, INSTRUMENT),
        (LABEL, LABEL),
        (PLACE, PLACE),
        (RECORDING, RECORDING),
        (RELEASE_GROUP, RELEASE_GROUP),
        (SERIES, SERIES),
        (WORK, WORK),)
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    entity_type = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'editor_collection_type'


models.signals.pre_save.connect(
    pre_save_editor_collection_type, sender=editor_collection_type)
