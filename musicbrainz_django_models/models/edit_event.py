"""
.. module:: edit_event

The **Edit Event** Model.

PostgreSQL Definition
---------------------

The :code:`edit_event` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_event
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        event               INTEGER NOT NULL  -- PK, references event.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_event(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param event: references :class:`.event`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    event = models.OneToOneField('event')

    def __str__(self):
        return 'Edit Event'

    class Meta:
        db_table = 'edit_event'
