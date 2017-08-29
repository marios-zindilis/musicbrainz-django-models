"""
.. module:: editor_collection_event

The **Editor Collection Event** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_event` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_event (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        event INTEGER NOT NULL -- PK, references event.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_event(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param event: References :class:`event`.
    """

    event = models.ForeignKey('event')

    def __str__(self):
        return 'Editor Collection Event'

    class Meta:
        db_table = 'editor_collection_event'
