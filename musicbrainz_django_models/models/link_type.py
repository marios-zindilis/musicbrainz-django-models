"""
.. module:: link_type

The **Link Type** Model.

PostgreSQL Definition
---------------------

The :code:`link_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE link_type ( -- replicate
        id                  SERIAL,
        parent              INTEGER, -- references link_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        gid                 UUID NOT NULL,
        entity_type0        VARCHAR(50) NOT NULL,
        entity_type1        VARCHAR(50) NOT NULL,
        name                VARCHAR(255) NOT NULL,
        description         TEXT,
        link_phrase         VARCHAR(255) NOT NULL,
        reverse_link_phrase VARCHAR(255) NOT NULL,
        long_link_phrase    VARCHAR(255) NOT NULL,
        priority            INTEGER NOT NULL DEFAULT 0,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        is_deprecated       BOOLEAN NOT NULL DEFAULT false,
        has_dates           BOOLEAN NOT NULL DEFAULT true,
        entity0_cardinality INTEGER NOT NULL DEFAULT 0,
        entity1_cardinality INTEGER NOT NULL DEFAULT 0
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class link_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    gid = models.UUIDField(default=uuid.uuid4)
    entity_type0 = models.CharField(max_length=50)
    entity_type1 = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    link_phrase = models.CharField(max_length=255)
    reverse_link_phrase = models.CharField(max_length=255)
    long_link_phrase = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    is_deprecated = models.BooleanField(default=False)
    has_dates = models.BooleanField(default=True)
    entity0_cardinality = models.IntegerField(default=0)
    entity1_cardinality = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'link_type'
