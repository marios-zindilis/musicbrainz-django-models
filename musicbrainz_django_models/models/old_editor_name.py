"""
.. module:: old_editor_name

The **Old Editor Name** Model.

PostgreSQL Definition
---------------------

The :code:`old_editor_name` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE old_editor_name (
        name    VARCHAR(64) NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class old_editor_name(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'old_editor_name'
