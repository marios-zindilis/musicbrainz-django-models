"""
.. module:: editor_collection_work

The **Editor Collection Work** Model.

PostgreSQL Definition
---------------------

The :code:`editor_collection_work` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_collection_work (
        collection INTEGER NOT NULL, -- PK, references editor_collection.id
        work INTEGER NOT NULL -- PK, references work.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__editor_collection_model import abstract__editor_collection_model


@python_2_unicode_compatible
class editor_collection_work(abstract__editor_collection_model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`work`.
    """

    work = models.ForeignKey('work')

    def __str__(self):
        return 'Editor Collection Work'

    class Meta:
        db_table = 'editor_collection_work'
