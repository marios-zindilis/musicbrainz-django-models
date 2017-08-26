"""
.. module:: work_meta

The **Work Meta** Model.

PostgreSQL Definition
---------------------

The :code:`work_meta` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_meta ( -- replicate
        id                  INTEGER NOT NULL, -- PK, references work.id CASCADE
        rating              SMALLINT CHECK (rating >= 0 AND rating <= 100),
        rating_count        INTEGER
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_meta import abstract__model_meta


@python_2_unicode_compatible
class work_meta(abstract__model_meta):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param int id: references :class:`.work`. This is both a foreign and a
        primary key, best implemented in Django as a `OneToOneField`.
    """

    id = models.OneToOneField('work', primary_key=True)

    def __str__(self):
        return 'Work Meta'

    class Meta:
        db_table = 'work_meta'
