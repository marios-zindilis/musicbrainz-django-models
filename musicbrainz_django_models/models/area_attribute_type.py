"""
.. module:: area_attribute_type

The **Area Attribute Type** Model.

PostgreSQL Definition
---------------------

The :code:`area_attribute_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_attribute_type ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        name                VARCHAR(255) NOT NULL,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        free_text           BOOLEAN NOT NULL,
        parent              INTEGER, -- references area_attribute_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from . import abstract


class area_attribute_type(abstract.model_attribute_type):
    class Meta:
        db_table = 'area_attribute_type'
