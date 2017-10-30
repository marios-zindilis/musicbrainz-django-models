"""
.. module:: work_annotation

The **Work Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`work_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_annotation ( -- replicate (verbose)
        work                INTEGER NOT NULL, -- PK, references work.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class work_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`work`.
    :param annotation: References :class:`annotation`.
    """

    work = models.OneToOneField('work', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Work Annotation'

    class Meta:
        db_table = 'work_annotation'
