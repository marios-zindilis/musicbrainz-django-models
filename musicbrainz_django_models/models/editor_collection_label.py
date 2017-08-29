"""
.. module:: editor_collection_label

The **Editor Collection Label** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_label` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_label (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        label INTEGER NOT NULL -- PK, references label.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_label(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param label: References :class:`label`.
    """

    label = models.ForeignKey('label')

    def __str__(self):
        return 'Editor Collection Label'

    class Meta:
        db_table = 'editor_collection_label'
