"""
.. module:: artist_credit_name

The **Artist Credit Name** Model.

PostgreSQL Definition
---------------------

The :code:`artist_credit_name` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_credit_name ( -- replicate (verbose)
        artist_credit       INTEGER NOT NULL, -- PK, references artist_credit.id CASCADE
        position            SMALLINT NOT NULL, -- PK
        artist              INTEGER NOT NULL, -- references artist.id CASCADE
        name                VARCHAR NOT NULL,
        join_phrase         TEXT NOT NULL DEFAULT ''
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class artist_credit_name(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    artist_credit = models.OneToOneField('artist_credit', primary_key=True)
    position = models.SmallIntegerField(unique=True)
    artist = models.ForeignKey('artist')
    name = models.CharField(max_length=255)
    join_phrase = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist_credit_name'
