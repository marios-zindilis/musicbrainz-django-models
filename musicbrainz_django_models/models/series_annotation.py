"""
.. module:: series_annotation

The **Series Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`series_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_annotation ( -- replicate (verbose)
        series              INTEGER NOT NULL, -- PK, references series.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class series_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param series: References :class:`series`.
    :param annotation: References :class:`annotation`.
    """

    series = models.OneToOneField('series', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Series Annotation'

    class Meta:
        db_table = 'series_annotation'
