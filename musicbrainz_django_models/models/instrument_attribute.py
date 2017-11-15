"""
.. module:: instrument_attribute

The **Instrument Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`instrument_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        instrument                                INTEGER NOT NULL, -- references instrument.id
        instrument_attribute_type                 INTEGER NOT NULL, -- references instrument_attribute_type.id
        instrument_attribute_type_allowed_value   INTEGER, -- references instrument_attribute_type_allowed_value.id
        instrument_attribute_text                 TEXT
        CHECK (
            (instrument_attribute_type_allowed_value IS NULL AND instrument_attribute_text IS NOT NULL)
            OR
            (instrument_attribute_type_allowed_value IS NOT NULL AND instrument_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class instrument_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param instrument: References :class:`instrument`
    :param instrument_attribute_type: References :class:`instrument_attribute_type`
    :param instrument_attribute_type_allowed_value: References :class:`instrument_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    instrument = models.ForeignKey('instrument')
    instrument_attribute_type = models.ForeignKey('instrument_attribute_type')
    instrument_attribute_type_allowed_value = models.ForeignKey('instrument_attribute_type_allowed_value', null=True)
    instrument_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Instrument Attribute'

    class Meta:
        db_table = 'instrument_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=instrument_attribute)
