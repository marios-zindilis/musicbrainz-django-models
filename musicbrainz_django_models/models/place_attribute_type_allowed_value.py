"""
.. module:: place_attribute_type_allowed_value

The **Place Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`place_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        place_attribute_type        INTEGER NOT NULL, -- references place_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references place_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class place_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param place_attribute_type: References :class:`place_attribute_type`.
    """

    place_attribute_type = models.ForeignKey('place_attribute_type')

    def __str__(self):
        return 'Place Attribute Type Allowed Value'

    class Meta:
        db_table = 'place_attribute_type_allowed_value'
