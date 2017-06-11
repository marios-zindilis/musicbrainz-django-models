"""
.. module:: edit_work

The **Edit Work** Model.

PostgreSQL Definition
---------------------

The :code:`edit_work` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_work
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        work                INTEGER NOT NULL  -- PK, references work.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_work(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param work: references :class:`.work`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    work = models.OneToOneField('work')

    def __str__(self):
        return 'Edit Work'

    class Meta:
        db_table = 'edit_work'
