"""
.. module:: model_attribute_type

This Abstract Django Model is subclassed by:

1.  :class:`area_attribute_type`
2.  :class:`artist_attribute_type`
3.  :class:`event_attribute_type`
4.  :class:`instrument_attribute_type`
5.  :class:`label_attribute_type`
6.  :class:`medium_attribute_type`
7.  :class:`place_attribute_type`
8.  :class:`recording_attribute_type`
9.  :class:`release_attribute_type`
10. :class:`release_group_attribute_type`
11. :class:`series_attribute_type`
12. :class:`work_attribute_type`

These models are defined in the MusicBrainz Server as:

    CREATE TABLE <MODEL>_attribute_type ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        name                VARCHAR(255) NOT NULL,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        free_text           BOOLEAN NOT NULL,
        parent              INTEGER, -- references <MODEL>_attribute_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class model_attribute_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, default='')
    free_text = models.BooleanField()
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
