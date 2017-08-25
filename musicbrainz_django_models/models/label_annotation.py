"""
.. module:: label_annotation

The **Label Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`label_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_annotation ( -- replicate (verbose)
        label               INTEGER NOT NULL, -- PK, references label.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class label_annotation(models.Model):
    label = models.OneToOneField('label', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Label Annotation'

    class Meta:
        db_table = 'label_annotation'
