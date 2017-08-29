"""
.. module:: editor_collection_release

The **Editor Collection Release** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_release` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_release (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        release INTEGER NOT NULL -- PK, references release.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_release(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release`
    """

    release = models.ForeignKey('release')

    def __str__(self):
        return 'Editor Collection Release'

    class Meta:
        db_table = 'editor_collection_release'
