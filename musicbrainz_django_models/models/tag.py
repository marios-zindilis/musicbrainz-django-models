"""
.. module:: tag

The **Tag** Model.

PostgreSQL Definition
---------------------

The :code:`tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE tag ( -- replicate (verbose)
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        ref_count           INTEGER NOT NULL DEFAULT 0
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class tag(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ref_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
