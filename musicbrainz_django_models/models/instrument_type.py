"""
.. module:: instrument_type

The **Instrument Type** Model is referenced by the :code:`instrument` model.

PostgreSQL Definition
---------------------

The :code:`instrument_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_type ( -- replicate
        id                  SERIAL, -- PK
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references instrument_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL 
    );

"""

from django.db import models
import uuid


class instrument_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'instrument_type'
