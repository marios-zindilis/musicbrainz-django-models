"""
.. module:: edit

The **Edit** Model.

PostgreSQL Definition
---------------------

The :code:`edit` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id
        type                SMALLINT NOT NULL,
        status              SMALLINT NOT NULL,
        autoedit            SMALLINT NOT NULL DEFAULT 0,
        open_time            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        close_time           TIMESTAMP WITH TIME ZONE,
        expire_time          TIMESTAMP WITH TIME ZONE NOT NULL,
        language            INTEGER, -- references language.id
        quality             SMALLINT NOT NULL DEFAULT 1
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    autoedit = models.SmallIntegerField(default=0)
    open_time = models.DateTimeField(auto_now=True)
    close_time = models.DateTimeField(null=True)
    expire_time = models.DateTimeField()
    language = models.ForeignKey('language')
    quality = models.SmallIntegerField(default=1)

    def __str__(self):
        return 'Edit'

    class Meta:
        db_table = 'edit'
