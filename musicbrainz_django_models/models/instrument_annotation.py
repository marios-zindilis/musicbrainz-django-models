"""
.. module:: instrument_annotation

The **Instrument Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`instrument_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_annotation ( -- replicate (verbose)
        instrument  INTEGER NOT NULL, -- PK, references instrument.id
        annotation  INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class instrument_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    instrument = models.OneToOneField('instrument', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Instrument Annotation'

    class Meta:
        db_table = 'instrument_annotation'
