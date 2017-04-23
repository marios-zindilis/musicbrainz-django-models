"""
.. module:: instrument

The **Instrument** Model.

PostgreSQL Definition
---------------------

The :code:`instrument` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument ( -- replicate (verbose)
        id              SERIAL, -- PK
        gid             uuid NOT NULL,
        name            VARCHAR NOT NULL,
        type            INTEGER, -- references instrument_type.id
        edits_pending   INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >=0),
        last_updated    TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        comment         VARCHAR(255) NOT NULL DEFAULT '',
        description     TEXT NOT NULL DEFAULT ''
    );

"""

from django.db import models
import uuid


class instrument(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    type = models.ForeignKey('instrument_type')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255, default='')
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'instrument'
