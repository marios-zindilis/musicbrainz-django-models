"""
.. module:: abstract__editor_collection_model

This is an Abstract Django Model, meant to be subclassed by Models that store
MusicBrainz editors' collections in the same way, namely:

1.  :class:`editor_collection_area`
2.  :class:`editor_collection_artist`
3.  :class:`editor_collection_event`
4.  :class:`editor_collection_instrument`
5.  :class:`editor_collection_label`
6.  :class:`editor_collection_place`
7.  :class:`editor_collection_recording`
8.  :class:`editor_collection_release`
9.  :class:`editor_collection_release_group`
10. :class:`editor_collection_series`
11. :class:`editor_collection_work`

Those models are defined in the MusicBrainz Servers as:

.. code-block:: sql

    CREATE TABLE editor_collection_<MODEL> (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        <MODEL> INTEGER NOT NULL -- PK, references <MODEL>.id
    );

"""

from django.db import models


class abstract__editor_collection_model(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param collection: References :class:`editor_collection`.
    """

    collection = models.OneToOneField('editor_collection', primary_key=True)

    class Meta:
        abstract = True
