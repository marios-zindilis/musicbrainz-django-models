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
from .abstract__model_alias_type import abstract__model_alias_type


@python_2_unicode_compatible
class work_alias_type(abstract__model_alias_type):
    class Meta:
        db_table = 'work_alias_type'
