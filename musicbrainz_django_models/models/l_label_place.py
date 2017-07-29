"""
.. module:: l_label_place

The **L Label Place** Model.

PostgreSQL Definition
---------------------

The :code:`l_label_place` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE l_label_place ( -- replicate
        id                  SERIAL,
        link                INTEGER NOT NULL, -- references link.id
        entity0             INTEGER NOT NULL, -- references label.id
        entity1             INTEGER NOT NULL, -- references place.id
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        link_order          INTEGER NOT NULL DEFAULT 0 CHECK (link_order >= 0),
        entity0_credit      TEXT NOT NULL DEFAULT '',
        entity1_credit      TEXT NOT NULL DEFAULT ''
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class l_label_place(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param int link_order: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    """

    id = models.AutoField(primary_key=True)
    link = models.ForeignKey('link')
    entity0 = models.ForeignKey('label', related_name='links_to_place')
    entity1 = models.ForeignKey('place')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    link_order = models.PositiveIntegerField(default=0)
    entity0 = models.TextField(default='')
    entity1 = models.TextField(default='')

    def __str__(self):
        return 'L Label Place'

    class Meta:
        db_table = 'l_label_place'
