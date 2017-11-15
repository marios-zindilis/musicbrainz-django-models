"""
.. module:: recording_attribute_type_allowed_value

The **Recording Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`recording_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE recording_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        recording_attribute_type    INTEGER NOT NULL, -- references recording_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references recording_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class recording_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param recording_attribute_type: References :class:`recording_attribute_type`.
    """

    recording_attribute_type = models.ForeignKey('recording_attribute_type')

    def __str__(self):
        return 'Recording Attribute Type Allowed Value'

    class Meta:
        db_table = 'recording_attribute_type_allowed_value'
