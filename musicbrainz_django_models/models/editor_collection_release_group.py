"""
.. module:: editor_collection_release_group

The **Editor Collection Release Group** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_release_group` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_release_group (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        release_group INTEGER NOT NULL -- PK, references release_group.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_release_group(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group: References :class:`release_group`
    """

    release_group = models.ForeignKey('release_group')

    def __str__(self):
        return 'Editor Collection Release Group'

    class Meta:
        db_table = 'editor_collection_release_group'
