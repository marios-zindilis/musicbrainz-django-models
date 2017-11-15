"""
.. module:: instrument_attribute_type_allowed_value

The **Instrument Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`instrument_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        instrument_attribute_type   INTEGER NOT NULL, -- references instrument_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references instrument_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class instrument_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param instrument_attribute_type: References :class:`instrument_attribute_type`.
    """

    instrument_attribute_type = models.ForeignKey('instrument_attribute_type')

    def __str__(self):
        return 'Instrument Attribute Type Allowed Value'

    class Meta:
        db_table = 'instrument_attribute_type_allowed_value'
