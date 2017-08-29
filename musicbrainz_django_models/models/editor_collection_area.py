"""
.. module:: editor_collection_area

The **Editor Collection Area** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_area` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_area (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        area INTEGER NOT NULL -- PK, references area.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_area(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param area: References :class:`area`.
    """

    area = models.OneToOneField('area')

    def __str__(self):
        return 'Editor Collection Area'

    class Meta:
        db_table = 'editor_collection_area'
