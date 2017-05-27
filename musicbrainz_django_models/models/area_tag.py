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


@python_2_unicode_compatible
class area_tag(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param area: references :class:`.area`
    :param tag: references :class:`.tag`
    """

    area = models.ForeignKey('area')
    tag = models.ForeignKey('tag')
    count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Area Tag'

    class Meta:
        db_table = 'area_tag'
