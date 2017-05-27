"""
.. module:: artist_annotation

The **Artist Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`artist_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_annotation ( -- replicate (verbose)
        artist              INTEGER NOT NULL, -- PK, references artist.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class artist_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    The `artist` and `annotation` fields are both primary and foreign keys. In
    Django, there can only be one primary key per model. This is best
    implemented using `OneToOneField` fields.
    """

    artist = models.OneToOneField('artist')
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Artist Annotation'

    class Meta:
        db_table = 'artist_annotation'
