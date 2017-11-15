"""
.. module:: recording_attribute

The **Recording Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`recording_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE recording_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        recording                                INTEGER NOT NULL, -- references recording.id
        recording_attribute_type                 INTEGER NOT NULL, -- references recording_attribute_type.id
        recording_attribute_type_allowed_value   INTEGER, -- references recording_attribute_type_allowed_value.id
        recording_attribute_text                 TEXT
        CHECK (
            (recording_attribute_type_allowed_value IS NULL AND recording_attribute_text IS NOT NULL)
            OR
            (recording_attribute_type_allowed_value IS NOT NULL AND recording_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class recording_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param recording: References :class:`recording`
    :param recording_attribute_type: References :class:`recording_attribute_type`
    :param recording_attribute_type_allowed_value: References :class:`recording_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    recording = models.ForeignKey('recording')
    recording_attribute_type = models.ForeignKey('recording_attribute_type')
    recording_attribute_type_allowed_value = models.ForeignKey('recording_attribute_type_allowed_value', null=True)
    recording_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Recording Attribute'

    class Meta:
        db_table = 'recording_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=recording_attribute)
