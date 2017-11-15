"""
.. module:: artist_attribute_type

The **Artist Attribute Type** Model.

PostgreSQL Definition
---------------------

The :code:`artist_attribute_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_attribute_type ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        name                VARCHAR(255) NOT NULL,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        free_text           BOOLEAN NOT NULL,
        parent              INTEGER, -- references artist_attribute_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.utils.encoding import python_2_unicode_compatible
from . import abstract


@python_2_unicode_compatible
class artist_attribute_type(abstract.model_attribute_type):
    class Meta:
        db_table = 'artist_attribute_type'
