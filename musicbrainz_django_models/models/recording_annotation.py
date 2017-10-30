"""
.. module:: recording_annotation

The **Recording Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`recording_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE recording_annotation ( -- replicate (verbose)
        recording           INTEGER NOT NULL, -- PK, references recording.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class recording_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param recording: References :class:`recording`.
    :param annotation: References :class:`annotation`.
    """

    recording = models.OneToOneField('recording', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Recording Annotation'

    class Meta:
        db_table = 'recording_annotation'
