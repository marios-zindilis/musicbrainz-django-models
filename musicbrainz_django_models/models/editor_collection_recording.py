"""
.. module:: editor_collection_recording

The **Editor Collection Recording** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_recording` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_recording (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        recording INTEGER NOT NULL -- PK, references recording.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_recording(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param recording: References :class:`recording`.
    """

    recording = models.OneToOneField('recording')

    def __str__(self):
        return 'Editor Collection Recording'

    class Meta:
        db_table = 'editor_collection_recording'
