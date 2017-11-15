"""
.. module:: artist_attribute

The **Artist Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`artist_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        artist                                INTEGER NOT NULL, -- references artist.id
        artist_attribute_type                 INTEGER NOT NULL, -- references artist_attribute_type.id
        artist_attribute_type_allowed_value   INTEGER, -- references artist_attribute_type_allowed_value.id
        artist_attribute_text                 TEXT
        CHECK (
            (artist_attribute_type_allowed_value IS NULL AND artist_attribute_text IS NOT NULL)
            OR
            (artist_attribute_type_allowed_value IS NOT NULL AND artist_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_model_attribute


@python_2_unicode_compatible
class artist_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param artist: References :class:`artist`
    :param artist_attribute_type: References :class:`artist_attribute_type`
    :param artist_attribute_type_allowed_value: References :class:`artist_attribute_type_allowed_value`.
    """

    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey('artist')
    artist_attribute_type = models.ForeignKey('artist_attribute_type')
    artist_attribute_type_allowed_value = models.ForeignKey('artist_attribute_type_allowed_value', null=True)
    artist_attribute_text = models.TextField(null=True)

    def __str__(self):
        return 'Artist Attribute'

    class Meta:
        db_table = 'artist_attribute'


models.signals.pre_save.connect(pre_save_model_attribute, sender=artist_attribute)
