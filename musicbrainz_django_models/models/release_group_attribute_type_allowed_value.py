"""
.. module:: release_group_attribute_type_allowed_value

The **Release Group Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_attribute_type_allowed_value ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        release_group_attribute_type        INTEGER NOT NULL, -- references release_group_attribute_type.id
        value                               TEXT,
        parent                              INTEGER, -- references release_group_attribute_type_allowed_value.id
        child_order                         INTEGER NOT NULL DEFAULT 0,
        description                         TEXT,
        gid                                 uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class release_group_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group_attribute_type: References :class:`release_group_attribute_type`.
    """

    release_group_attribute_type = models.ForeignKey('release_group_attribute_type')

    def __str__(self):
        return 'Release Group Attribute Type Allowed Value'

    class Meta:
        db_table = 'release_group_attribute_type_allowed_value'
