"""
.. module:: editor

The **Editor** model.

PostgreSQL Definition
---------------------

The :code:`editor` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor
    (
        id                  SERIAL,
        name                VARCHAR(64) NOT NULL,
        privs               INTEGER DEFAULT 0,
        email               VARCHAR(64) DEFAULT NULL,
        website             VARCHAR(255) DEFAULT NULL,
        bio                 TEXT DEFAULT NULL,
        member_since        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        email_confirm_date  TIMESTAMP WITH TIME ZONE,
        last_login_date     TIMESTAMP WITH TIME ZONE DEFAULT now(),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        birth_date          DATE,
        gender              INTEGER, -- references gender.id
        area                INTEGER, -- references area.id
        password            VARCHAR(128) NOT NULL,
        ha1                 CHAR(32) NOT NULL,
        deleted             BOOLEAN NOT NULL DEFAULT FALSE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    privs = models.IntegerField(default=0)
    email = models.CharField(max_length=64, null=True)
    website = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    member_since = models.DateTimeField(auto_now=True)
    email_confirm_date = models.DateTimeField(null=True)
    last_login_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)
    birth_date = models.DateField(null=True)
    gender = models.ForeignKey('gender', null=True)
    area = models.ForeignKey('area', null=True)
    password = models.CharField(max_length=128)
    ha1 = models.CharField(max_length=32)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'editor'
