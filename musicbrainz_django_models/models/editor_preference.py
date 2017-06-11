"""
.. module:: editor_preference

The **Editor Preference** Model.

PostgreSQL Definition
---------------------

The :code:`editor_preference` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_preference
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id
        name                VARCHAR(50) NOT NULL,
        value               VARCHAR(100) NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_preference(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`.editor`
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    def __str__(self):
        return 'Editor Preference'

    class Meta:
        db_table = 'editor_preference'
