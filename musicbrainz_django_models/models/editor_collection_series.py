"""
.. module:: editor_collection_series

The **Editor Collection Series** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_series` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_series (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        series INTEGER NOT NULL -- PK, references series.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_series(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param series: References :class:`series`.
    """

    series = models.ForeignKey('series')

    def __str__(self):
        return 'Editor Collection Series'

    class Meta:
        db_table = 'editor_collection_series'
