"""
.. module:: recording_tag

The **Recording Tag** Model.

PostgreSQL Definition
---------------------

The :code:`recording_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE recording_tag ( -- replicate (verbose)
        recording           INTEGER NOT NULL, -- PK, references recording.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class recording_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param recording: References :class:`recording`.
    """

    recording = models.OneToOneField('recording', primary_key=True)

    def __str__(self):
        return 'Recording Tag'

    class Meta:
        db_table = 'recording_tag'
