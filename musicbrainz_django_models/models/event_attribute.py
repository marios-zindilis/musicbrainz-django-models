"""
.. module:: event_attribute

The **Event Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`event_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        event                                INTEGER NOT NULL, -- references event.id
        event_attribute_type                 INTEGER NOT NULL, -- references event_attribute_type.id
        event_attribute_type_allowed_value   INTEGER, -- references event_attribute_type_allowed_value.id
        event_attribute_text                 TEXT
        CHECK (
            (event_attribute_type_allowed_value IS NULL AND event_attribute_text IS NOT NULL)
            OR
            (event_attribute_type_allowed_value IS NOT NULL AND event_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class event_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param event: References :class:`event`
    :param event_attribute_type: References :class:`event_attribute_type`
    :param event_attribute_type_allowed_value: References :class:`event_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('event')
    event_attribute_type = models.ForeignKey('event_attribute_type')
    event_attribute_type_allowed_value = models.ForeignKey('event_attribute_type_allowed_value', null=True)
    event_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Event Attribute'

    class Meta:
        db_table = 'event_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=event_attribute)
