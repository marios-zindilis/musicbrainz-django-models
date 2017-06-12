"""
.. module:: editor_subscribe_editor

The **Editor Subscribe Editor** Model.

PostgreSQL Definition
---------------------

The :code:`editor_subscribe_editor` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_subscribe_editor
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id (the one who has subscribed)
        subscribed_editor   INTEGER NOT NULL, -- references editor.id (the one being subscribed)
        last_edit_sent      INTEGER NOT NULL  -- weakly references edit.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_subscribe_editor(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`.editor` (the one who has subscribed)
    :param subscribed_editor: references :class:`.editor` (the one being subscribed to)
    :param last_edit_sent: references :class:`.edit`
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    subscribed_editor = models.ForeignKey('editor', related_name='subscribers')
    last_edit_sent = models.ForeignKey('edit')

    def __str__(self):
        return 'Editor Subscribe Editor'

    class Meta:
        db_table = 'editor_subscribe_editor'
