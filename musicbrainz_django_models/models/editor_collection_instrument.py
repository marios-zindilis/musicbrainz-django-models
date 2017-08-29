"""
.. module:: editor_collection_instrument

The **Editor Collection Instrument** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_instrument` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_instrument (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        instrument INTEGER NOT NULL -- PK, references instrument.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_instrument(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param instrument: References :class:`instrument`.
    """

    instrument = models.ForeignKey('instrument')

    def __str__(self):
        return 'Editor Collection Instrument'

    class Meta:
        db_table = 'editor_collection_instrument'
