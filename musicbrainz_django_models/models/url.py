"""
.. module:: url

The **Url** Model.

PostgreSQL Definition
---------------------

The :code:`url` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE url ( -- replicate
        id                  SERIAL,
        gid                 UUID NOT NULL,
        url                 TEXT NOT NULL,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class url(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param url: A `TEXT` field is used in the Postgres definition for the URL.
        In Django, there is a `URLField` which is more or less a `TextField`
        with added regular expression validation for URLs and a default
        `max_length` of 200. The longest URL in the MusicBrainz database dump
        in late April 2017 was 1524 characters.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    url = models.URLField(max_length=2000)
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'url'
