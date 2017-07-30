"""
.. module:: vote

The **Vote** Model.

PostgreSQL Definition
---------------------

The :code:`vote` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE vote
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id
        edit                INTEGER NOT NULL, -- references edit.id
        vote                SMALLINT NOT NULL,
        vote_time            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        superseded          BOOLEAN NOT NULL DEFAULT FALSE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class vote(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    edit = models.ForeignKey('edit')
    vote = models.SmallIntegerField()
    vote_time = models.DateTimeField(auto_now=True)
    superseded = models.BooleanField(default=False)

    def __str__(self):
        return 'Vote'

    class Meta:
        db_table = 'vote'
