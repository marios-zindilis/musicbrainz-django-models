"""
.. module:: abstract__model_gid_redirect

This is an Abstract Django Model, meant to be subclassed by Models that store
redirects in the same way, namely:

1.  :class:`area_gid_redirect`
2.  :class:`artist_gid_redirect`
3.  :class:`event_gid_redirect`
4.  :class:`instrument_gid_redirect`
5.  :class:`label_gid_redirect`
6.  :class:`place_gid_redirect`
7.  :class:`recording_gid_redirect`
8.  :class:`release_gid_redirect`
9.  :class:`release_group_gid_redirect`
10. :class:`series_gid_redirect`
11. :class:`track_gid_redirect`
12. :class:`url_gid_redirect`
13. :class:`work_gid_redirect`


Those models are defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_gid_redirect ( -- replicate (verbose)
        gid         UUID NOT NULL, -- PK
        new_id      INTEGER NOT NULL, -- references <MODEL>.id
        created     TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
import uuid


class abstract__model_gid_redirect(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    gid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
