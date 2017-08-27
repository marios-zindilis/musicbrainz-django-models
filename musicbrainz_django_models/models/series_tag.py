"""
.. module:: series_tag

The **Series Tag** Model.

PostgreSQL Definition
---------------------

The :code:`series_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_tag ( -- replicate (verbose)
        series              INTEGER NOT NULL, -- PK, references series.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class series_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param series: References :class:`series`.
    """

    series = models.OneToOneField('series', primary_key=True)

    def __str__(self):
        return 'Series Tag'

    class Meta:
        db_table = 'series_tag'
