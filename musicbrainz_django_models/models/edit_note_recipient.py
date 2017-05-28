"""
.. module:: edit_note_recipient

The **Edit Note Recipient** Model.

PostgreSQL Definition
---------------------

The :code:`edit_note_recipient` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_note_recipient (
        recipient           INTEGER NOT NULL, -- PK, references editor.id
        edit_note           INTEGER NOT NULL  -- PK, references edit_note.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_note_recipient(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    recipient = models.OneToOneField('editor', primary_key=True)
    edit_note = models.OneToOneField('edit_note')

    def __str__(self):
        return 'Edit Note Recipient'

    class Meta:
        db_table = 'edit_note_recipient'
