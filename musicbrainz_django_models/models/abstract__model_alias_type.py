"""
.. module:: abstract__model_alias_type

This is an Abstract Django Model, meant to be subclassed by Models that store
the *type* of other models' aliases, namely:

1.  :class:`area_alias_type`
2.  :class:`artist_alias_type`
3.  :class:`event_alias_type`
4.  :class:`instrument_alias_type`
5.  :class:`label_alias_type`
6.  :class:`place_alias_type`
7.  :class:`recording_alias_type`
8.  :class:`release_alias_type`
9.  :class:`release_group_alias_type`
10. :class:`series_alias_type`
11. :class:`work_alias_type`

These models are defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references <MODEL>_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
import uuid


class abstract__model_alias_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
