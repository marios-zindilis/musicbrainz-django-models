"""
.. module:: editor_collection

The **Editor Collection** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection
    (
        id                  SERIAL,
        gid                 UUID NOT NULL,
        editor              INTEGER NOT NULL, -- references editor.id
        name                VARCHAR NOT NULL,
        public              BOOLEAN NOT NULL DEFAULT FALSE,
        description         TEXT DEFAULT '' NOT NULL,
        type                INTEGER NOT NULL -- references editor_collection_type.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class editor_collection(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    editor = models.ForeignKey('editor')
    name = models.CharField(max_length=255)
    public = models.BooleanField(default=False)
    description = models.TextField(default='')
    type = models.ForeignKey('editor_collection_type')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'editor_collection'
