"""
.. module:: edit_instrument

The **Edit Instrument** Model.

PostgreSQL Definition
---------------------

The :code:`edit_instrument` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_instrument
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        instrument          INTEGER NOT NULL  -- PK, references instrument.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_instrument(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    edit = models.OneToOneField('edit', primary_key=True)
    instrument = models.OneToOneField('instrument')

    def __str__(self):
        return 'Edit Instrument'

    class Meta:
        db_table = 'edit_instrument'
