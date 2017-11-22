"""
.. module:: recording_alias_type

The **Recording Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`recording_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE recording_alias_type ( -- replicate
        id                  SERIAL, -- PK,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references recording_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.utils.encoding import python_2_unicode_compatible
from . import abstract


@python_2_unicode_compatible
class recording_alias_type(abstract.model_type):
    class Meta:
        db_table = 'recording_alias_type'
