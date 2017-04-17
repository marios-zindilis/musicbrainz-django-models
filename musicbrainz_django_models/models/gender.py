"""
.. module:: gender

The **Gender** Model is referenced by the :code:`artist` and the
:code:`editor` models. Here's a not necessarily complete table of values:

+--------------------------------------+--------+
| gid                                  | name   |
+======================================+========+
| 93452b5a-a947-30c8-934f-6a4056b151c2 | Female |
+--------------------------------------+--------+
| 36d3d30a-839d-3eda-8cb3-29be4384e4a9 | Male   |
+--------------------------------------+--------+

PostgreSQL Definition
---------------------

The :code:`gender` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE gender ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references gender.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL 
    );

"""

from django.db import models
import uuid


class gender(models.Model):
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
        db_table = 'gender'
