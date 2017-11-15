"""
.. module:: place_attribute

The **Place Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`place_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        place                                INTEGER NOT NULL, -- references place.id
        place_attribute_type                 INTEGER NOT NULL, -- references place_attribute_type.id
        place_attribute_type_allowed_value   INTEGER, -- references place_attribute_type_allowed_value.id
        place_attribute_text                 TEXT
        CHECK (
            (place_attribute_type_allowed_value IS NULL AND place_attribute_text IS NOT NULL)
            OR
            (place_attribute_type_allowed_value IS NOT NULL AND place_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class place_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param place: References :class:`place`
    :param place_attribute_type: References :class:`place_attribute_type`
    :param place_attribute_type_allowed_value: References :class:`place_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    place = models.ForeignKey('place')
    place_attribute_type = models.ForeignKey('place_attribute_type')
    place_attribute_type_allowed_value = models.ForeignKey('place_attribute_type_allowed_value', null=True)
    place_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Place Attribute'

    class Meta:
        db_table = 'place_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=place_attribute)
