"""
.. module:: label_attribute_type_allowed_value

The **Label Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`label_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        label_attribute_type        INTEGER NOT NULL, -- references label_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references label_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class label_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param label_attribute_type: References :class:`label_attribute_type`.
    """

    label_attribute_type = models.ForeignKey('label_attribute_type')

    def __str__(self):
        return 'Label Attribute Type Allowed Value'

    class Meta:
        db_table = 'label_attribute_type_allowed_value'
