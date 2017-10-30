"""
.. module:: release_meta

The **Release Meta** Model.

PostgreSQL Definition
---------------------

The :code:`release_meta` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_meta ( -- replicate (verbose)
        id                  INTEGER NOT NULL, -- PK, references release.id CASCADE
        date_added          TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        info_url            VARCHAR(255),
        amazon_asin         VARCHAR(10),
        amazon_store        VARCHAR(20),
        cover_art_presence  cover_art_presence NOT NULL DEFAULT 'absent'
    );

    CREATE TYPE cover_art_presence AS ENUM ('absent', 'present', 'darkened');

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_meta(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param id: References :class:`release`.
    :param cover_art_presence: In the PostgreSQL definition, the type of this
        field references a `TYPE` with the same name. In Django, this can be
        implemented with `choices`.
    """

    ABSENT = 'absent'
    PRESENT = 'present'
    DARKENED = 'darkened'
    COVER_ART_PRESENCE_CHOICES = (
        (ABSENT, ABSENT),
        (PRESENT, PRESENT),
        (DARKENED, DARKENED))

    id = models.OneToOneField('release', primary_key=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    info_url = models.CharField(max_length=255, null=True)
    amazon_asin = models.CharField(max_length=10, null=True)
    amazon_store = models.CharField(max_length=20, null=True)
    cover_art_presense = models.CharField(max_length=8, default=ABSENT)

    def __str__(self):
        return 'Release Meta'

    class Meta:
        db_table = 'release_meta'
