"""
.. module:: work_attribute_type_allowed_value

The **Work Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`work_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_attribute_type_allowed_value ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        work_attribute_type INTEGER NOT NULL, -- references work_attribute_type.id
        value               TEXT,
        parent              INTEGER, -- references work_attribute_type_allowed_value.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class work_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work_attribute_type: References :class:`work_attribute_type`.
    """

    work_attribute_type = models.ForeignKey('work_attribute_type')

    def __str__(self):
        return 'Work Attribute Type Allowed Value'

    class Meta:
        db_table = 'work_attribute_type_allowed_value'
