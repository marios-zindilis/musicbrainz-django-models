"""
.. module:: medium_attribute_type_allowed_value_allowed_format

The **Medium Attribute Type Allowed Value Allowed Format** Model.

PostgreSQL Definition
---------------------

The :code:`medium_attribute_type_allowed_value_allowed_format` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE medium_attribute_type_allowed_value_allowed_format ( -- replicate (verbose)
        medium_format INTEGER NOT NULL, -- PK, references medium_format.id,
        medium_attribute_type_allowed_value INTEGER NOT NULL -- PK, references medium_attribute_type_allowed_value.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class medium_attribute_type_allowed_value_allowed_format(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param medium_format: References :class:`medium_format`
    :param medium_attribute_type_allowed_value: References :class:`medium_attribute_type_allowed_value`
    """

    medium_format = models.OneToOneField('medium_format', primary_key=True)
    medium_attribute_type_allowed_value = models.OneToOneField('medium_attribute_type_allowed_value')

    def __str__(self):
        return 'Medium Attribute Type Allowed Value Allowed Format'

    class Meta:
        db_table = 'medium_attribute_type_allowed_value_allowed_format'
