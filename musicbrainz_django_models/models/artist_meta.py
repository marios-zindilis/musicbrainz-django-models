"""
.. module:: artist_meta

The **Artist Meta** Model.

PostgreSQL Definition
---------------------

The :code:`artist_meta` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_meta ( -- replicate
        id                  INTEGER NOT NULL, -- PK, references artist.id CASCADE
        rating              SMALLINT CHECK (rating >= 0 AND rating <= 100),
        rating_count        INTEGER
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_meta import abstract__model_meta


@python_2_unicode_compatible
class artist_meta(abstract__model_meta):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param int id: references :class:`.artist`. This is both a foreign and a
        primary key, best implemented in Django as a `OneToOneField`.
    """

    id = models.OneToOneField('artist', primary_key=True)

    def __str__(self):
        return 'Artist Meta'

    class Meta:
        db_table = 'artist_meta'
