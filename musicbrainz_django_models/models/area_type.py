"""
The :code:`area_type` table defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_type ( -- replicate
        id                  SERIAL, -- PK
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references area_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models


class area_type(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=0)
    gid = models.UUIDField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'area_type'
