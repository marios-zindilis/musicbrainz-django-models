"""
.. module:: iso_3166_1

The **Iso 3166 1** Model.

PostgreSQL Definition
---------------------

The :code:`iso_3166_1` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE iso_3166_1 ( -- replicate
        area      INTEGER NOT NULL, -- references area.id
        code      CHAR(2) -- PK
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class iso_3166_1(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    area = models.ForeignKey('area')
    code = models.CharField(max_length=2, primary_key=True)

    def __str__(self):
        return 'ISO 3166_1'

    class Meta:
        db_table = 'iso_3166_1'
