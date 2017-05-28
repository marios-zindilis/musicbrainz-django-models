"""
.. module:: release_raw

The **Release Raw** Model.

PostgreSQL Definition
---------------------

The :code:`release_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_raw ( -- replicate
        id                  SERIAL, -- PK
        title               VARCHAR(255) NOT NULL,
        artist              VARCHAR(255),
        added               TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        last_modified        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        lookup_count         INTEGER DEFAULT 0,
        modify_count         INTEGER DEFAULT 0,
        source              INTEGER DEFAULT 0,
        barcode             VARCHAR(255),
        comment             VARCHAR(255) NOT NULL DEFAULT ''
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    lookup_count = models.IntegerField(default=0)
    modify_count = models.IntegerField(default=0)
    source = models.IntegerField(default=0)
    barcode = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'release_raw'
