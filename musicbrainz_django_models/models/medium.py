"""
.. module:: medium

The **Medium** model.

PostgreSQL Definition
---------------------

The :code:`medium` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE medium ( -- replicate (verbose)
        id                  SERIAL,
        release             INTEGER NOT NULL, -- references release.id
        position            INTEGER NOT NULL,
        format              INTEGER, -- references medium_format.id
        name                VARCHAR NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        track_count         INTEGER NOT NULL DEFAULT 0
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class medium(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: The maximum length is mandatory in Django but not in
        PostgreSQL.
    """

    id = models.AutoField(primary_key=True)
    release = models.ForeignKey('release')
    position = models.IntegerField()
    format = models.ForeignKey('medium_format')
    name = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    track_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'medium'
        verbose_name_plural = 'Media'
