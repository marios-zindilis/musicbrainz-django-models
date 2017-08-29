"""
.. module:: editor_collection_artist

The **Editor Collection Artist** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_artist` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_artist (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        artist INTEGER NOT NULL -- PK, references artist.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_artist(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param artist: References :class:`artist`
    """

    artist = models.ForeignKey('artist')

    def __str__(self):
        return 'Editor Collection Artist'

    class Meta:
        db_table = 'editor_collection_artist'
