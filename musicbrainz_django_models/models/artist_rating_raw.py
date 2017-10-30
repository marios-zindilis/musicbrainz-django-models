"""
.. module:: artist_rating_raw

The **Artist Rating Raw** Model.

PostgreSQL Definition
---------------------

The :code:`artist_rating_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_rating_raw
    (
        artist              INTEGER NOT NULL, -- PK, references artist.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        rating              SMALLINT NOT NULL CHECK (rating >= 0 AND rating <= 100)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_rating_raw import abstract__model_rating_raw


@python_2_unicode_compatible
class artist_rating_raw(abstract__model_rating_raw):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param artist: References :class:`artist`.
    """

    artist = models.OneToOneField('artist', primary_key=True)

    def __str__(self):
        return 'Artist Rating Raw'

    class Meta:
        db_table = 'artist_rating_raw'
