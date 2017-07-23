"""
.. module:: event_annotation

The **Event Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`event_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_annotation ( -- replicate (verbose)
        event               INTEGER NOT NULL, -- PK, references event.id
        annotation          INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class event_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param event: references :class:`.event`
    :param annotation: references :class:`.annotation`
    """

    event = models.OneToOneField('event', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Event Annotation'

    class Meta:
        db_table = 'event_annotation'
