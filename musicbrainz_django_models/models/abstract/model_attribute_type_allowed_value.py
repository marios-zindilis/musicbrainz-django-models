"""
.. module:: model_attribute_type_allowed_value

This Abstract Django Model is subclassed by:

1.  :class:`area_attribute_type_allowed_value`
2.  :class:`artist_attribute_type_allowed_value`
3.  :class:`event_attribute_type_allowed_value`
4.  :class:`instrument_attribute_type_allowed_value`
5.  :class:`label_attribute_type_allowed_value`
6.  :class:`medium_attribute_type_allowed_value`
7.  :class:`place_attribute_type_allowed_value`
8.  :class:`recording_attribute_type_allowed_value`
9.  :class:`release_attribute_type_allowed_value`
10. :class:`release_group_attribute_type_allowed_value`
11. :class:`series_attribute_type_allowed_value`
12. :class:`work_attribute_type_allowed_value`

These models are defined in the MusicBrainz Server as:

    CREATE TABLE <MODEL>_attribute_type_allowed_value ( -- replicate (verbose)
        id                      SERIAL,  -- PK
        <MODEL>_attribute_type  INTEGER NOT NULL, -- references area_attribute_type.id
        value                   TEXT,
        parent                  INTEGER, -- references area_attribute_type_allowed_value.id
        child_order             INTEGER NOT NULL DEFAULT 0,
        description             TEXT,
        gid                     uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class model_attribute_type_allowed_value(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    id = models.AutoField(primary_key=True)
    value = models.TextField(null=True)
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    class Meta:
        abstract = True
