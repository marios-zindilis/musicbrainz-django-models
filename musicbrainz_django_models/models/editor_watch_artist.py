"""
.. module:: editor_watch_artist

The **Editor Watch Artist** Model.

PostgreSQL Definition
---------------------

The :code:`editor_watch_artist` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_watch_artist
    (
        artist INTEGER NOT NULL, -- PK, references artist.id CASCADE
        editor INTEGER NOT NULL  -- PK, references editor.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_watch_artist(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`editor`. This is both a foreign key to
        the Editor model, as well as a primary key in this model,  nicely
        implemented in Django as a OneToOneField.
    """

    editor = models.OneToOneField('editor', primary_key=True)
    artist = models.OneToOneField('artist')

    def __str__(self):
        return '{editor} watches {artist}'.format(
            editor=str(self.editor),
            artist=str(self.artist))

    class Meta:
        db_table = 'editor_watch_artist'
