"""
.. module:: editor_watch_release_status

The **Editor Watch Release Status** Model.

PostgreSQL Definition
---------------------

The :code:`editor_watch_release_status` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_watch_release_status
    (
        editor INTEGER NOT NULL, -- PK, references editor.id CASCADE
        release_status INTEGER NOT NULL -- PK, references release_status.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_watch_release_status(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`editor`. This is both a foreign key to
        the Editor model, as well as a primary key in this model,  nicely
        implemented in Django as a OneToOneField.
    """

    editor = models.OneToOneField('editor', primary_key=True)
    release_status = models.OneToOneField('release_status')

    def __str__(self):
        return '{editor} watches {release_status}'.format(
            editor=str(self.editor),
            release_status=str(self.release_status))

    class Meta:
        db_table = 'editor_watch_release_status'
