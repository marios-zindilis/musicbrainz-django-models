"""
.. module:: event_alias_type

The **Event Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`event_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references event_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
import uuid


def pre_save_event_alias_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICES_LIST:
        raise ValidationError('Name "{}" not one of {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICES_LIST)))


@python_2_unicode_compatible
class event_alias_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    EVENT_NAME = 'Event name'
    SEARCH_HINT = 'Search hint'
    NAME_CHOICES = (
        (EVENT_NAME, EVENT_NAME),
        (SEARCH_HINT, SEARCH_HINT))
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.TextField(choices=NAME_CHOICES)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    decription = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'event_alias_type'


models.signals.pre_save.connect(
    pre_save_event_alias_type, sender=event_alias_type)
