"""
.. module:: artist_tag_raw

The **Artist Tag Raw** Model.

PostgreSQL Definition
---------------------

The :code:`artist_tag_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_tag_raw
    (
        artist              INTEGER NOT NULL, -- PK, references artist.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        is_upvote           BOOLEAN NOT NULL DEFAULT TRUE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag_raw import abstract__model_tag_raw


@python_2_unicode_compatible
class artist_tag_raw(abstract__model_tag_raw):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param artist: References :class:`artist`.
    """

    artist = models.OneToOneField('artist', primary_key=True)

    def __str__(self):
        return 'Artist Tag Raw'

    class Meta:
        db_table = 'artist_tag_raw'
