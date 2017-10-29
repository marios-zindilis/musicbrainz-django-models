"""
.. module:: place_annotation

The **Place Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`place_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place_annotation ( -- replicate (verbose)
        place       INTEGER NOT NULL, -- PK, references place.id
        annotation  INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class place_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param place: References :class:`place`.
    :param annotation: References :class:`annotation`.
    """

    place = models.OneToOneField('place', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Place Annotation'

    class Meta:
        db_table = 'place_annotation'
