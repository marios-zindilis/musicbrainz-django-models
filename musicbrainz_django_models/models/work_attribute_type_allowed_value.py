"""
.. module:: work_attribute_type_allowed_value

The **Work Attribute Type Allowed Value** Model.

PostgreSQL Definition
---------------------

The :code:`work_attribute_type_allowed_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_attribute_type_allowed_value ( -- replicate (verbose)
        id                  SERIAL,  -- PK
        work_attribute_type INTEGER NOT NULL, -- references work_attribute_type.id
        value               TEXT,
        parent              INTEGER, -- references work_attribute_type_allowed_value.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class work_attribute_type_allowed_value(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    id = models.AutoField(primary_key=True)
    work_attribute_type = models.ForeignKey('work_attribute_type')
    value = models.TextField(null=True)
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return 'Work Attribute Type Allowed Value'

    class Meta:
        db_table = 'work_attribute_type_allowed_value'
