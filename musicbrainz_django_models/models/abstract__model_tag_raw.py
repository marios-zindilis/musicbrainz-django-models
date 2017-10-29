"""
.. module:: abstract__model_tag_raw

This is an Abstract Django Model, meant to be subclassed by Models that store
raw tags in the same way, namely:

1.  :class:`area_tag_raw`
2.  :class:`artist_tag_raw`
3.  :class:`event_tag_raw`
4.  :class:`instrument_tag_raw`
5.  :class:`label_tag_raw
6.  :class:`place_tag_raw`
7.  :class:`recording_tag_raw`
8.  :class:`release_tag_raw`
9.  :class:`release_group_tag_raw`
10. :class:`series_tag_raw`
11. :class:`work_tag_raw`

Those models are defined in the MusicBrainz server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_tag_raw
    (
        <MODEL>     INTEGER NOT NULL, -- PK, references <MODEL>.id
        editor      INTEGER NOT NULL, -- PK, references editor.id
        tag         INTEGER NOT NULL, -- PK, references tag.id
        is_upvote   BOOLEAN NOT NULL DEFAULT TRUE
    );

"""

from django.db import models


class abstract__model_tag_raw(models.Model):
    editor = models.OneToOneField('editor')
    tag = models.OneToOneField('tag')
    is_upvote = models.BooleanField(default=True)

    class Meta:
        abstract = True
