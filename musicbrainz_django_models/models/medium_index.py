"""
.. module:: medium_index

The **Medium Index** Model.

PostgreSQL Definition
---------------------

The :code:`medium_index` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE medium_index ( -- replicate
        medium              INTEGER, -- PK, references medium.id CASCADE
        toc                 CUBE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class medium_index(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param medium: References :class:`medium`.
    :param toc: This uses a PostgreSQL-specific data type of `CUBE`. For now,
        I'm creating this as a TEXT field.
    """

    medium = models.OneToOneField('medium', primary_key=True)
    toc = models.TextField()

    def __str__(self):
        return 'Medium Index'

    class Meta:
        db_table = 'medium_index'
