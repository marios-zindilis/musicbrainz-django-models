"""
.. module:: series_attribute_type_allowed_value

The **Series Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`series_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        series_attribute_type       INTEGER NOT NULL, -- references series_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references series_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class series_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param series_attribute_type: References :class:`series_attribute_type`.
    """

    series_attribute_type = models.ForeignKey('series_attribute_type')

    def __str__(self):
        return 'Series Attribute Type Allowed Value'

    class Meta:
        db_table = 'series_attribute_type_allowed_value'
