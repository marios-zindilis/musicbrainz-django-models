"""
.. module:: medium_cdtoc

The **Medium Cdtoc** Model.

PostgreSQL Definition
---------------------

The :code:`medium_cdtoc` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE medium_cdtoc ( -- replicate (verbose)
        id                  SERIAL,
        medium              INTEGER NOT NULL, -- references medium.id
        cdtoc               INTEGER NOT NULL, -- references cdtoc.id
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class medium_cdtoc(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param medium: References :class:`medium`.
    :param cdtoc: References :class:`cdtoc`.
    """

    id = models.AutoField(primary_key=True)
    medium = models.ForeignKey('medium')
    cdtoc = models.ForeignKey('cdtoc')
    edits_pending = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Medium CDTOC'

    class Meta:
        db_table = 'medium_cdtoc'
