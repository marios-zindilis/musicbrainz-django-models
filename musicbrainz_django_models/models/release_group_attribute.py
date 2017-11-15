"""
.. module:: release_group_attribute

The **Release Group Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_attribute ( -- replicate (verbose)
        id                                          SERIAL,  -- PK
        release_group                               INTEGER NOT NULL, -- references release_group.id
        release_group_attribute_type                INTEGER NOT NULL, -- references release_group_attribute_type.id
        release_group_attribute_type_allowed_value  INTEGER, -- references release_group_attribute_type_allowed_value.id
        release_group_attribute_text                TEXT
        CHECK (
            (release_group_attribute_type_allowed_value IS NULL AND release_group_attribute_text IS NOT NULL)
            OR
            (release_group_attribute_type_allowed_value IS NOT NULL AND release_group_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class release_group_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group: References :class:`release_group`
    :param release_group_attribute_type: References :class:`release_group_attribute_type`
    :param release_group_attribute_type_allowed_value: References :class:`release_group_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    release_group = models.ForeignKey('release_group')
    release_group_attribute_type = models.ForeignKey('release_group_attribute_type')
    release_group_attribute_type_allowed_value = models.ForeignKey(
        'release_group_attribute_type_allowed_value',
        null=True)
    release_group_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Release Group Attribute'

    class Meta:
        db_table = 'release_group_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=release_group_attribute)
