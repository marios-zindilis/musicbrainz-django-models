"""
.. module:: release_attribute

The **Release Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`release_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        release                                INTEGER NOT NULL, -- references release.id
        release_attribute_type                 INTEGER NOT NULL, -- references release_attribute_type.id
        release_attribute_type_allowed_value   INTEGER, -- references release_attribute_type_allowed_value.id
        release_attribute_text                 TEXT
        CHECK (
            (release_attribute_type_allowed_value IS NULL AND release_attribute_text IS NOT NULL)
            OR
            (release_attribute_type_allowed_value IS NOT NULL AND release_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class release_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release`
    :param release_attribute_type: References :class:`release_attribute_type`
    :param release_attribute_type_allowed_value: References :class:`release_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    release = models.ForeignKey('release')
    release_attribute_type = models.ForeignKey('release_attribute_type')
    release_attribute_type_allowed_value = models.ForeignKey('release_attribute_type_allowed_value', null=True)
    release_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Release Attribute'

    class Meta:
        db_table = 'release_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=release_attribute)
