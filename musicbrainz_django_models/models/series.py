"""
.. module:: series

The **Series** Model.

PostgreSQL Definition
---------------------

The :code:`series` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        type                INTEGER NOT NULL, -- references series_type.id
        ordering_attribute  INTEGER NOT NULL, -- references link_text_attribute_type.attribute_type
        ordering_type       INTEGER NOT NULL, -- references series_ordering_type.id
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class series(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, default='')
    type = models.ForeignKey('series_type')
    ordering_attribute = models.ForeignKey('link_text_attribute_type')
    ordering_type = models.ForeignKey('series_ordering_type')
    edits_pending = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'series'
