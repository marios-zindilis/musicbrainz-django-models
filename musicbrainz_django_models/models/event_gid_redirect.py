"""
.. module:: event_gid_redirect

The **Event Gid Redirect** Model.

PostgreSQL Definition
---------------------

The :code:`event_gid_redirect` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_gid_redirect ( -- replicate (verbose)
        gid                 UUID NOT NULL, -- PK
        new_id              INTEGER NOT NULL, -- references event.id
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class event_gid_redirect(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    gid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    new_id = models.ForeignKey('event')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Event GID Redirect'

    class Meta:
        db_table = 'event_gid_redirect'
