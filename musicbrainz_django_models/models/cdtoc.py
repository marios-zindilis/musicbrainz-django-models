"""
.. module:: cdtoc

The **Cdtoc** Model.

PostgreSQL Definition
---------------------

The :code:`cdtoc` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE cdtoc ( -- replicate
        id                  SERIAL,
        discid              CHAR(28) NOT NULL,
        freedb_id           CHAR(8) NOT NULL,
        track_count         INTEGER NOT NULL,
        leadout_offset      INTEGER NOT NULL,
        track_offset        INTEGER[] NOT NULL,
        degraded            BOOLEAN NOT NULL DEFAULT FALSE,
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class cdtoc(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param track_offset: This field uses a Postgres-specific data type in the
        SQL definition, that stores an array of integers. In a Django app that
        is written to be used exclusively with Postgres, it is possible to
        implement this with an `ArrayField()` from the
        `django.contrib.postgres.fields`. In this specific case, the array
        that is stored seems to comprise `track` IDs, so this could be well
        implemented as a `ManyToManyField`. However, to maintain compatibility
        with the MusicBrainz schema, and to retain the ability to import data
        from the MusicBrainz database dumps, this is implemented here as a
        `CharField`, that can then be split. The values stored in this field
        look like this: `{123,567,980}`.

        As of around April 2017, the CD TOC with the longest stored list of
        tracks (as in the amount of characters in the database) is
        https://musicbrainz.org/cdtoc/RVwHSnjyt0eKWq_KBoidX9N.wRc- with 688
        characters used in the `track_offset` field.
    """

    id = models.AutoField(primary_key=True)
    discid = models.CharField(max_length=28)
    freedb_id = models.CharField(max_length=8)
    track_count = models.IntegerField()
    leadout_offset = models.IntegerField()
    track_offset = models.CharField(max_length=1024)
    degraded = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'CD TOC'

    class Meta:
        db_table = 'cdtoc'
