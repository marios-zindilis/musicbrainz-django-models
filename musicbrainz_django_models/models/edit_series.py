"""
.. module:: edit_series

The **Edit Series** Model.

PostgreSQL Definition
---------------------

The :code:`edit_series` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_series
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        series              INTEGER NOT NULL  -- PK, references series.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_series(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param series: references :class:`.series`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    series = models.OneToOneField('series')

    def __str__(self):
        return 'Edit Series'

    class Meta:
        db_table = 'edit_series'
