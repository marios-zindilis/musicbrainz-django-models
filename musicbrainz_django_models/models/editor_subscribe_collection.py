"""
.. module:: editor_subscribe_collection

The **Editor Subscribe Collection** Model.

PostgreSQL Definition
---------------------

The :code:`editor_subscribe_collection` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_subscribe_collection
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL,              -- references editor.id
        collection          INTEGER NOT NULL,              -- weakly references editor_collection.id
        last_edit_sent      INTEGER NOT NULL,              -- weakly references edit.id
        available           BOOLEAN NOT NULL DEFAULT TRUE,
        last_seen_name      VARCHAR(255)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_subscribe_collection(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    collection = models.ForeignKey('editor_collection')
    last_edit_sent = models.ForeignKey('edit')
    available = models.BooleanField(default=True)
    last_seen_name = models.CharField(max_length=255)

    def __str__(self):
        return 'Editor Subscribe Collection'

    class Meta:
        db_table = 'editor_subscribe_collection'
