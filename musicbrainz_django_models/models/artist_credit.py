"""
.. module:: artist_credit

The **Artist Credit** model

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
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    artist_count = models.SmallIntegerField()
    ref_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist_credit'
