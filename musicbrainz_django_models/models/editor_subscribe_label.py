"""
.. module:: editor_subscribe_label

The **Editor Subscribe Label** Model.

PostgreSQL Definition
---------------------

The :code:`editor_subscribe_label` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_subscribe_label
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id
        label               INTEGER NOT NULL, -- references label.id
        last_edit_sent      INTEGER NOT NULL -- references edit.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_subscribe_label(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`.editor`
    :param label: references :class:`.label`
    :param last_edit_sent: references :class:`.edit`
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    label = models.ForeignKey('label')
    last_edit_sent = models.ForeignKey('edit')

    def __str__(self):
        return 'Editor Subscribe Label'

    class Meta:
        db_table = 'editor_subscribe_label'
