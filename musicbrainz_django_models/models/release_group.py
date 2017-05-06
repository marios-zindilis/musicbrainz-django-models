"""
.. module:: release_group

The **Release Group** model. Read more about `Release Groups on MusicBrainz`_.

.. _Release Groups on MusicBrainz: https://musicbrainz.org/doc/Release_Group

PostgreSQL Definition
---------------------

The :code:`release_group` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        artist_credit       INTEGER NOT NULL, -- references artist_credit.id
        type                INTEGER, -- references release_group_primary_type.id
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class release_group(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    artist_credit = models.ForeignKey('artist_credit')
    type = models.ForeignKey('release_group_primary_type')
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'release_group'
        verbose_name_plural = 'Release Groups'
