"""
.. module:: medium_attribute_type_allowed_value

The **Medium Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`medium_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE medium_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        medium_attribute_type       INTEGER NOT NULL, -- references medium_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references medium_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class medium_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param medium_attribute_type: References :class:`medium_attribute_type`.
    """

    medium_attribute_type = models.ForeignKey('medium_attribute_type')

    def __str__(self):
        return 'Medium Attribute Type Allowed Value'

    class Meta:
        db_table = 'medium_attribute_type_allowed_value'
