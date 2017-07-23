"""
.. module:: event_tag

The **Event Tag** Model.

PostgreSQL Definition
---------------------

The :code:`event_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_tag ( -- replicate (verbose)
        event               INTEGER NOT NULL, -- PK, references event.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class event_tag(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    event = models.OneToOneField('event', primary_key=True)
    tag = models.OneToOneField('tag')
    count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Event Tag'

    class Meta:
        db_table = 'event_tag'
