"""
.. module:: medium_format

The **Medium Format** model.

PostgreSQL Definition
---------------------

The :code:`medium_format` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE medium_format ( -- replicate
        id                  SERIAL,
        name                VARCHAR(100) NOT NULL,
        parent              INTEGER, -- references medium_format.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        year                SMALLINT,
        has_discids         BOOLEAN NOT NULL DEFAULT FALSE,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class medium_format(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('medium_format', null=True)
    child_order = models.IntegerField(default=0)
    year = models.SmallIntegerField(null=True)
    has_discids = models.BooleanField(default=False)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'medium_format'
        verbose_name_plural = 'Medium Formats'
