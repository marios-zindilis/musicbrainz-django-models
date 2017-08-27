"""
.. module:: abstract__model_tag

This is an Abstract Django Model, meant to be subclassed by Models that store
tags in the same way, namely:

1.  :class:`area_tag`
2.  :class:`artist_tag`
3.  :class:`event_tag`
4.  :class:`instrument_tag`
5.  :class:`label_tag`
6.  :class:`place_tag`
7.  :class:`recording_tag`
8.  :class:`release_tag`
9.  :class:`release_group_tag`
10. :class:`series_tag`
11. :class:`work_tag`

Those models are defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_tag ( -- replicate (verbose)
        <MODEL>         INTEGER NOT NULL, -- PK, references <MODEL>.id
        tag             INTEGER NOT NULL, -- PK, references tag.id
        count           INTEGER NOT NULL,
        last_updated    TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models


class abstract__model_tag(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param tag: This field is both a Foreign Key to the :class:`tag` Model, as
        well as a Primary Key of each `<MODEL>_tag` model. In Django, this is
        best implemented as a `OneToOneField`.
    """

    tag = models.OneToOneField('tag')
    count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
