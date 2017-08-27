"""
.. module:: area_tag

The **Area Tag** Model.

PostgreSQL Definition
---------------------

The :code:`area_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_tag ( -- replicate (verbose)
        area                INTEGER NOT NULL, -- PK, references area.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class area_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param area: references :class:`.area`
    """

    area = models.OneToOneField('area', primary_key=True)

    def __str__(self):
        return 'Area Tag'

    class Meta:
        db_table = 'area_tag'
