"""
.. module:: edit_recording

The **Edit Recording** Model.

PostgreSQL Definition
---------------------

The :code:`edit_recording` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_recording
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        recording           INTEGER NOT NULL  -- PK, references recording.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_recording(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param recording: references :class:`.recording`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    recording = models.OneToOneField('recording')

    def __str__(self):
        return 'Edit Recording'

    class Meta:
        db_table = 'edit_recording'
