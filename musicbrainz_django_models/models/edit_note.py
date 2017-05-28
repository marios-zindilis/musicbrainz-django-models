"""
.. module:: edit_note

The **Edit Note** Model.

PostgreSQL Definition
---------------------

The :code:`edit_note` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_note
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id
        edit                INTEGER NOT NULL, -- references edit.id
        text                TEXT NOT NULL,
        post_time            TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_note(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`.editor`
    :param edit: references :class:`.edit`
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    edit = models.ForeignKey('edit')
    text = models.TextField()
    post_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Edit Note'

    class Meta:
        db_table = 'edit_note'
