"""
.. module:: work_attribute_type

The **Work Attribute Type** Model.

PostgreSQL Definition
---------------------

The :code:`work_attribute_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_attribute_type ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        name                VARCHAR(255) NOT NULL,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        free_text           BOOLEAN NOT NULL,
        parent              INTEGER, -- references work_attribute_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class work_attribute_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, default='')
    free_text = models.BooleanField()
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'work_attribute_type'
