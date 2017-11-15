"""
.. module:: artist_attribute_type_allowed_value

The **Artist Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`artist_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        artist_attribute_type       INTEGER NOT NULL, -- references artist_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references artist_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class artist_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param artist_attribute_type: References :class:`artist_attribute_type`
    """

    artist_attribute_type = models.ForeignKey('artist_attribute_type')

    def __str__(self):
        return 'Artist Attribute Type Allowed Value'

    class Meta:
        db_table = 'artist_attribute_type_allowed_value'
