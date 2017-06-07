"""
.. module:: edit_release

The **Edit Release** Model.

PostgreSQL Definition
---------------------

The :code:`edit_release` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_release
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        release             INTEGER NOT NULL  -- PK, references release.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_release(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param release: references :class:`.release`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    release = models.OneToOneField('release')

    def __str__(self):
        return 'Edit Release'

    class Meta:
        db_table = 'edit_release'
