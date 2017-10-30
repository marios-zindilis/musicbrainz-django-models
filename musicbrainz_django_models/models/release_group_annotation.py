"""
.. module:: release_group_annotation

The **Release Group Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_annotation ( -- replicate (verbose)
        release_group       INTEGER NOT NULL, -- PK, references release_group.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_group_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group: References :class:`release_group`.
    :param annotation: References :class:`annotation`.
    """

    release_group = models.OneToOneField('release_group', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Release Group Annotation'

    class Meta:
        db_table = 'release_group_annotation'
