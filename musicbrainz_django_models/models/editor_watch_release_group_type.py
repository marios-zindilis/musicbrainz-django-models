"""
.. module:: editor_watch_release_group_type

The **Editor Watch Release Group Type** Model.

PostgreSQL Definition
---------------------

The :code:`editor_watch_release_group_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_watch_release_group_type
    (
        editor INTEGER NOT NULL, -- PK, references editor.id CASCADE
        release_group_type INTEGER NOT NULL -- PK, references release_group_primary_type.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_watch_release_group_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`editor`. This is both a foreign key to
        the Editor model, as well as a primary key in this model,  nicely
        implemented in Django as a OneToOneField.
    """

    editor = models.OneToOneField('editor', primary_key=True)
    release_group_type = models.OneToOneField('release_group_primary_type')

    def __str__(self):
        return '{editor} watches {release_group_type}'.format(
            editor=str(self.editor),
            release_group_type=str(self.release_group_type))

    class Meta:
        db_table = 'editor_watch_release_group_type'
