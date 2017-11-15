"""
.. module:: series_attribute

The **Series Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`series_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        series                                INTEGER NOT NULL, -- references series.id
        series_attribute_type                 INTEGER NOT NULL, -- references series_attribute_type.id
        series_attribute_type_allowed_value   INTEGER, -- references series_attribute_type_allowed_value.id
        series_attribute_text                 TEXT
        CHECK (
            (series_attribute_type_allowed_value IS NULL AND series_attribute_text IS NOT NULL)
            OR
            (series_attribute_type_allowed_value IS NOT NULL AND series_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class series_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param series: References :class:`series`
    :param series_attribute_type: References :class:`series_attribute_type`
    :param series_attribute_type_allowed_value: References :class:`series_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    series = models.ForeignKey('series')
    series_attribute_type = models.ForeignKey('series_attribute_type')
    series_attribute_type_allowed_value = models.ForeignKey('series_attribute_type_allowed_value', null=True)
    series_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Series Attribute'

    class Meta:
        db_table = 'series_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=series_attribute)
