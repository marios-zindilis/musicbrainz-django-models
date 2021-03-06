"""
.. module:: artist_tag

The **Artist Tag** Model.

PostgreSQL Definition
---------------------

The :code:`artist_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_tag ( -- replicate (verbose)
        artist              INTEGER NOT NULL, -- PK, references artist.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class artist_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param artist: References :class:`artist`
    """

    artist = models.OneToOneField('artist', primary_key=True)

    def __str__(self):
        return 'Artist Tag'

    class Meta:
        db_table = 'artist_tag'
