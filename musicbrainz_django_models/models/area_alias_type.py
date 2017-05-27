"""
.. module:: area_alias_type

The **Area Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`area_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_alias_type ( -- replicate
        id                  SERIAL, -- PK,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references area_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class area_alias_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    name = models.TextField()
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'area_alias_type'
