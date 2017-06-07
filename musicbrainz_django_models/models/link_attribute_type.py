"""
.. module:: link_attribute_type

The **Link Attribute Type** Model.

PostgreSQL Definition
---------------------

The :code:`link_attribute_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE link_attribute_type ( -- replicate
        id                  SERIAL,
        parent              INTEGER, -- references link_attribute_type.id
        root                INTEGER NOT NULL, -- references link_attribute_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        gid                 UUID NOT NULL,
        name                VARCHAR(255) NOT NULL,
        description         TEXT,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class link_attribute_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', related_name='children', null=True)
    root = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'link_attribute_type'
