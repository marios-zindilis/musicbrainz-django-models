"""
.. module:: annotation

The **Annotation** model.

PostgreSQL Definition
---------------------

The :code:`annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE annotation ( -- replicate (verbose)
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id
        text                TEXT,
        changelog           VARCHAR(255),
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`.editor`
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    text = models.TextField(null=True)
    changelog = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Annotation'

    class Meta:
        db_table = 'annotation'
