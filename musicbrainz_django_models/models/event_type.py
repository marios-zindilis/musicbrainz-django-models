"""
.. module:: event_type

The **Event Type** Model.

PostgreSQL Definition
---------------------

The :code:`event_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_type ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references event_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.utils.encoding import python_2_unicode_compatible
from . import abstract


@python_2_unicode_compatible
class event_type(abstract.model_type):
    class Meta:
        db_table = 'event_type'
