"""
.. module:: area_attribute_type_allowed_value

The **Area Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`area_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_attribute_type_allowed_value ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        area_attribute_type INTEGER NOT NULL, -- references area_attribute_type.id
        value               TEXT,
        parent              INTEGER, -- references area_attribute_type_allowed_value.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class area_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param area_attribute_type: References :class:`area_attribute_type`.
    """

    area_attribute_type = models.ForeignKey('area_attribute_type')

    def __str__(self):
        return 'Area Attribute Type Allowed Value'

    class Meta:
        db_table = 'area_attribute_type_allowed_value'
