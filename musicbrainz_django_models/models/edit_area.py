"""
.. module:: edit_area

The **Edit Area** Model.

PostgreSQL Definition
---------------------

The :code:`edit_area` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_area
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        area                INTEGER NOT NULL  -- PK, references area.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_area(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param area: references :class:`.area`
    """

    edit = models.ForeignKey('edit')
    area = models.ForeignKey('area')

    def __str__(self):
        return 'Edit Area'

    class Meta:
        db_table = 'edit_area'
