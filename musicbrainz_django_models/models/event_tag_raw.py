"""
.. module:: event_tag_raw

The **Event Tag Raw** Model.

PostgreSQL Definition
---------------------

The :code:`event_tag_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_tag_raw (
        event               INTEGER NOT NULL, -- PK, references event.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        is_upvote           BOOLEAN NOT NULL DEFAULT TRUE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class event_tag_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param event: references :class:`.event`
    :param editor: references :class:`.editor`
    :param tag: references :class:`.tag`
    """

    event = models.OneToOneField('event', primary_key=True)
    editor = models.OneToOneField('editor')
    tag = models.OneToOneField('tag')
    is_upvote = models.BooleanField(default=True)

    def __str__(self):
        return 'Event Tag Raw'

    class Meta:
        db_table = 'event_tag_raw'
