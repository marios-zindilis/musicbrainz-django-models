"""
.. module:: work

The **Work** model.

PostgreSQL Definition
---------------------

The `work` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        type                INTEGER, -- references work_type.id
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class work(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    type = models.ForeignKey('work_type')
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'work'
