"""
.. module:: instrument_tag_raw

The **Instrument Tag Raw** Model.

PostgreSQL Definition
---------------------

The :code:`instrument_tag_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_tag_raw (
        instrument          INTEGER NOT NULL, -- PK, references instrument.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        is_upvote           BOOLEAN NOT NULL DEFAULT TRUE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class instrument_tag_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    instrument = models.OneToOneField('instrument', primary_key=True)
    editor = models.OneToOneField('editor')
    tag = models.OneToOneField('tag')
    is_upvote = models.BooleanField(default=True)

    def __str__(self):
        return 'Instrument Tag Raw'

    class Meta:
        db_table = 'instrument_tag_raw'
