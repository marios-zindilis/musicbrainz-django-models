"""
.. module:: abstract__model_type

This is an Abstract Django Model, meant to be subclassed by Models that store
the *type* of other models, or the *type* of other models' aliases, namely:

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
12. :class:`area_type`
13. :class:`artist_type`
14. :class:`event_type`
15. :class:`instrument_type`
16. :class:`label_type`
17. :class:`place_type`
18. :class:`series_type`
19. :class:`work_type`
20. :class:`release_group_primary_type`
21. :class:`release_group_secondary_type`
22. :class:`alternative_release_type`
23. :class:`series_ordering_type`

These models are defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references <MODEL>_alias_type.id <OR> <MODEL>_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
import uuid


class model_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """
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
