"""
.. module:: release_coverart

The **Release Coverart** Model.

PostgreSQL Definition
---------------------

The :code:`release_coverart` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_coverart
    (
        id                  INTEGER NOT NULL, -- PK, references release.id CASCADE
        last_updated        TIMESTAMP WITH TIME ZONE,
        cover_art_url       VARCHAR(255)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_coverart(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param id: References :class:`release`.
    """

    id = models.OneToOneField('release', primary_key=True, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    cover_art_url = models.CharField(max_length=255)

    def __str__(self):
        return 'Release CoverArt'

    class Meta:
        db_table = 'release_coverart'
