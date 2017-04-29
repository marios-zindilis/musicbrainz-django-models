"""
.. module:: work_type

The **Work Type** model.

PostreSQL Definition
--------------------

The :code:`work_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_type ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references work_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
import uuid


class work_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'work_type'
