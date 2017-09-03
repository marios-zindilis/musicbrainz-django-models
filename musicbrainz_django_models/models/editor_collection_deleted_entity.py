"""
.. module:: editor_collection_deleted_entity

The **Editor Collection Deleted Entity** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_deleted_entity` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_deleted_entity (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        gid UUID NOT NULL -- PK, references deleted_entity.gid
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_collection_deleted_entity(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param collection: References :class:`editor_collection`.
    :param gid: References :class:`deleted_entity`.
    """

    collection = models.OneToOneField('editor_collection', primary_key=True)
    gid = models.OneToOneField('deleted_entity')

    def __str__(self):
        return 'Editor Collection Deleted Entity'

    class Meta:
        db_table = 'editor_collection_deleted_entity'
