"""
.. module:: artist_credit

The **Artist Credit** model. Read more at the
`Artist Credit documentation on MusicBrainz`_.

.. _Artist Credit documentation on MusicBrainz: https://musicbrainz.org/doc/Artist_Credits

PostgreSQL Definition
---------------------

The :code:`artist_credit` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_credit ( -- replicate
        id                  SERIAL,
        name                VARCHAR NOT NULL,
        artist_count        SMALLINT NOT NULL,
        ref_count           INTEGER DEFAULT 0,
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models


class artist_credit(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int artist_count: This is defined as `NOT NULL` in the SQL, but
        there is no default value given. Looking at the database dump, all
        values are >= 1, so that default is used here.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    artist_count = models.SmallIntegerField(default=1)
    ref_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist_credit'
