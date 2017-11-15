"""
.. module:: medium_attribute

The **Medium Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`medium_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE medium_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        medium                                INTEGER NOT NULL, -- references medium.id
        medium_attribute_type                 INTEGER NOT NULL, -- references medium_attribute_type.id
        medium_attribute_type_allowed_value   INTEGER, -- references medium_attribute_type_allowed_value.id
        medium_attribute_text                 TEXT
        CHECK (
            (medium_attribute_type_allowed_value IS NULL AND medium_attribute_text IS NOT NULL)
            OR
            (medium_attribute_type_allowed_value IS NOT NULL AND medium_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class medium_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param medium: References :class:`medium`
    :param medium_attribute_type: References :class:`medium_attribute_type`
    :param medium_attribute_type_allowed_value: References :class:`medium_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    medium = models.ForeignKey('medium')
    medium_attribute_type = models.ForeignKey('medium_attribute_type')
    medium_attribute_type_allowed_value = models.ForeignKey('medium_attribute_type_allowed_value', null=True)
    medium_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Medium Attribute'

    class Meta:
        db_table = 'medium_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=medium_attribute)
