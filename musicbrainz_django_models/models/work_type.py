"""
.. module:: work_type

The **Work Type** model.

PostreSQL Definition
--------------------

The :code:`work_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_type ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references work_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_type import abstract__model_type


@python_2_unicode_compatible
class work_type(abstract__model_type):
    class Meta:
        db_table = 'work_type'
        verbose_name_plural = 'Work Types'
