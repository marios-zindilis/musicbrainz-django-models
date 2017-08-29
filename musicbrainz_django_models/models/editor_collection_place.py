"""
.. module:: editor_collection_place

The **Editor Collection Place** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_place` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_place (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        place INTEGER NOT NULL -- PK, references place.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_place(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param place: References :class:`place`.
    """

    place = models.ForeignKey('place')

    def __str__(self):
        return 'Editor Collection Place'

    class Meta:
        db_table = 'editor_collection_place'
