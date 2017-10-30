"""
.. module:: release_annotation

The **Release Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`release_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_annotation ( -- replicate (verbose)
        release             INTEGER NOT NULL, -- PK, references release.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release`.
    :param annotation: References :class:`annotation`.
    """

    release = models.OneToOneField('release', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Release Annotation'

    class Meta:
        db_table = 'release_annotation'
