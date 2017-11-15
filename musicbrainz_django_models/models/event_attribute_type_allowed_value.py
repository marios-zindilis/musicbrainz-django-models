"""
.. module:: event_attribute_type_allowed_value

The **Event Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`event_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_attribute_type_allowed_value ( -- replicate (verbose)
        id                          SERIAL,  -- PK
        event_attribute_type        INTEGER NOT NULL, -- references event_attribute_type.id
        value                       TEXT,
        parent                      INTEGER, -- references event_attribute_type_allowed_value.id
        child_order                 INTEGER NOT NULL DEFAULT 0,
        description                 TEXT,
        gid                         uuid NOT NULL
    );

"""

from django.db import models
from . import abstract


class event_attribute_type_allowed_value(abstract.model_attribute_type_allowed_value):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param event_attribute_type: References :class:`event_attribute_type`
    """

    event_attribute_type = models.ForeignKey('event_attribute_type')

    def __str__(self):
        return 'Event Attribute Type Allowed Value'

    class Meta:
        db_table = 'event_attribute_type_allowed_value'
