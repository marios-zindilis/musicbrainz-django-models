"""
.. module:: work_alias_type

The **Work Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`work_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references work_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.utils.encoding import python_2_unicode_compatible
from . import abstract


@python_2_unicode_compatible
class work_alias_type(abstract.model_type):
    class Meta:
        db_table = 'work_alias_type'
