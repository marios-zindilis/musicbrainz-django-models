"""
.. module:: edit_release_group

The **Edit Release Group** Model.

PostgreSQL Definition
---------------------

The :code:`edit_release_group` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_release_group
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        release_group       INTEGER NOT NULL  -- PK, references release_group.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_release_group(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param release_group: references :class:`.release_group`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    release_group = models.OneToOneField('release_group')

    def __str__(self):
        return 'Edit Release Group'

    class Meta:
        db_table = 'edit_release_group'
