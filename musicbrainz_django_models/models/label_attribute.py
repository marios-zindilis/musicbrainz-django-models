"""
.. module:: label_attribute

The **Label Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`label_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        label                                INTEGER NOT NULL, -- references label.id
        label_attribute_type                 INTEGER NOT NULL, -- references label_attribute_type.id
        label_attribute_type_allowed_value   INTEGER, -- references label_attribute_type_allowed_value.id
        label_attribute_text                 TEXT
        CHECK (
            (label_attribute_type_allowed_value IS NULL AND label_attribute_text IS NOT NULL)
            OR
            (label_attribute_type_allowed_value IS NOT NULL AND label_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class label_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param label: References :class:`label`
    :param label_attribute_type: References :class:`label_attribute_type`
    :param label_attribute_type_allowed_value: References :class:`label_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    label = models.ForeignKey('label')
    label_attribute_type = models.ForeignKey('label_attribute_type')
    label_attribute_type_allowed_value = models.ForeignKey('label_attribute_type_allowed_value', null=True)
    label_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Label Attribute'

    class Meta:
        db_table = 'label_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=label_attribute)
