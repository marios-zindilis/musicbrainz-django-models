"""
.. module:: track_raw

The **Track Raw** Model.

PostgreSQL Definition
---------------------

The :code:`track_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE track_raw ( -- replicate
        id                  SERIAL, -- PK
        release             INTEGER NOT NULL,   -- references release_raw.id
        title               VARCHAR(255) NOT NULL,
        artist              VARCHAR(255),   -- For VA albums, otherwise empty
        sequence            INTEGER NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class track_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release_raw`.
    """

    id = models.AutoField(primary_key=True)
    release = models.ForeignKey('release_raw')
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, null=True)
    sequence = models.IntegerField()

    def __str__(self):
        return 'Track Raw'

    class Meta:
        db_table = 'track_raw'
