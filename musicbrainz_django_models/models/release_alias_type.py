"""
.. module:: release_alias_type

The **Release Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`release_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_alias_type ( -- replicate
        id                  SERIAL, -- PK,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references release_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_alias_type import abstract__model_alias_type


@python_2_unicode_compatible
class release_alias_type(abstract__model_alias_type):
    class Meta:
        db_table = 'release_alias_type'
