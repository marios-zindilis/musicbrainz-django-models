"""
.. module:: edit_place

The **Edit Place** Model.

PostgreSQL Definition
---------------------

The :code:`edit_place` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_place
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        place               INTEGER NOT NULL  -- PK, references place.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_place(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param place: references :class:`.place`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    place = models.OneToOneField('place')

    def __str__(self):
        return 'Edit Place'

    class Meta:
        db_table = 'edit_place'
