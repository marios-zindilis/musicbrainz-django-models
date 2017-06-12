"""
.. module:: editor_subscribe_label_deleted

The **Editor Subscribe Label Deleted** Model.

PostgreSQL Definition
---------------------

The :code:`editor_subscribe_label_deleted` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_subscribe_label_deleted
    (
        editor INTEGER NOT NULL, -- PK, references editor.id
        gid UUID NOT NULL, -- PK, references deleted_entity.gid
        deleted_by INTEGER NOT NULL -- references edit.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_subscribe_label_deleted(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`.editor`
    :param gid: references :class:`.deleted_entity`
    :param deleted_by: references :class:`.edit`
    """

    editor = models.OneToOneField('editor', primary_key=True)
    gid = models.OneToOneField('deleted_entity')
    deleted_by = models.ForeignKey('edit')

    def __str__(self):
        return 'Editor Subscribe Label Deleted'

    class Meta:
        db_table = 'editor_subscribe_label_deleted'
