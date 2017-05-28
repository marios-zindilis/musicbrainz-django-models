"""
.. module:: country_area

The **Country Area** Model.

PostgreSQL Definition
---------------------

The :code:`country_area` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE country_area ( -- replicate (verbose)
        area                INTEGER -- PK, references area.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class country_area(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    area = models.OneToOneField('area', primary_key=True)

    def __str__(self):
        return self.area.name

    class Meta:
        db_table = 'country_area'
