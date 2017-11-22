"""
.. module:: instrument_type

The **Instrument Type** Model is referenced by the :code:`instrument` model.

PostgreSQL Definition
---------------------

The :code:`instrument_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_type ( -- replicate
        id                  SERIAL, -- PK
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references instrument_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.utils.encoding import python_2_unicode_compatible
from . import abstract


@python_2_unicode_compatible
class instrument_type(abstract.model_type):
    class Meta:
        db_table = 'instrument_type'
        verbose_name_plural = 'Instrument Types'
