"""
.. module:: replication_control

The **Replication Control** Model.

PostgreSQL Definition
---------------------

The :code:`replication_control` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE replication_control ( -- replicate
        id                              SERIAL,
        current_schema_sequence         INTEGER NOT NULL,
        current_replication_sequence    INTEGER,
        last_replication_date           TIMESTAMP WITH TIME ZONE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class replication_control(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    id = models.AutoField(primary_key=True)
    current_schema_sequence = models.IntegerField()
    current_replication_sequence = models.IntegerField(null=True)
    last_replication_date = models.DateTimeField(null=True)

    def __str__(self):
        return 'Replication Control'

    class Meta:
        db_table = 'replication_control'
