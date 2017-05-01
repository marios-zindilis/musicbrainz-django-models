"""
.. module:: release

The **Release** model. Read more at the
`Release documentation on MusicBrainz`_.

.. _Release documentation on MusicBrainz: https://musicbrainz.org/doc/Release

PostgreSQL Definition
---------------------

The :code:`release` table is defined in the MusicBrainz server as:

.. code-block:: sql

    CREATE TABLE release ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        artist_credit       INTEGER NOT NULL, -- references artist_credit.id
        release_group       INTEGER NOT NULL, -- references release_group.id
        status              INTEGER, -- references release_status.id
        packaging           INTEGER, -- references release_packaging.id
        language            INTEGER, -- references language.id
        script              INTEGER, -- references script.id
        barcode             VARCHAR(255),
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        quality             SMALLINT NOT NULL DEFAULT -1,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
import uuid


class release(models.Model):
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
    release_group = models.ForeignKey('release_group')
    status = models.ForeignKey('release_status', null=True)
    packaging = models.ForeignKey('release_packaging', null=True)
    language = models.ForeignKey('language', null=True)
    script = models.ForeignKey('script', null=True)
    barcode = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    quality = models.SmallIntegerField(default=-1)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'release'
