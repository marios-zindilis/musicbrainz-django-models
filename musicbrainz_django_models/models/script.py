"""
.. module:: script

The **Script** model.

PostgreSQL Definition
---------------------

.. code-block:: sql

    CREATE TABLE script ( -- replicate
        id                  SERIAL,
        iso_code            CHAR(4) NOT NULL, -- ISO 15924
        iso_number          CHAR(3) NOT NULL, -- ISO 15924
        name                VARCHAR(100) NOT NULL,
        frequency           INTEGER NOT NULL DEFAULT 0
    );

"""

from django.db import models


class script(models.Model):
    id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=4, help_text='ISO 15924')
    iso_number = models.CharField(max_length=3, help_text='ISO 15924')
    name = models.CharField(max_length=100)
    frequency = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'script'
