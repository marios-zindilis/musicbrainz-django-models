"""
.. module:: area_attribute

The **Area Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`area_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        area                                INTEGER NOT NULL, -- references area.id
        area_attribute_type                 INTEGER NOT NULL, -- references area_attribute_type.id
        area_attribute_type_allowed_value   INTEGER, -- references area_attribute_type_allowed_value.id
        area_attribute_text                 TEXT
        CHECK (
            (area_attribute_type_allowed_value IS NULL AND area_attribute_text IS NOT NULL)
            OR
            (area_attribute_type_allowed_value IS NOT NULL AND area_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class area_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param area: References :class:`area`
    :param area_attribute_type: References :class:`area_attribute_type`
    :param area_attribute_type_allowed_value: References :class:`area_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    area = models.ForeignKey('area')
    area_attribute_type = models.ForeignKey('area_attribute_type')
    area_attribute_type_allowed_value = models.ForeignKey('area_attribute_type_allowed_value', null=True)
    area_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Area Attribute'

    class Meta:
        db_table = 'area_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=area_attribute)
