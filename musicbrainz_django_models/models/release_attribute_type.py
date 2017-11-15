"""
.. module:: release_attribute_type

The **Release Attribute Type** Model.

PostgreSQL Definition
---------------------

The :code:`release_attribute_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_attribute_type ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        name                VARCHAR(255) NOT NULL,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        free_text           BOOLEAN NOT NULL,
        parent              INTEGER, -- references release_attribute_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from . import abstract


class release_attribute_type(abstract.model_attribute_type):
    class Meta:
        db_table = 'release_attribute_type'
