"""
.. module:: artist_gid_redirect

The **Artist Gid Redirect** Model.

PostgreSQL Definition
---------------------

The :code:`artist_gid_redirect` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_gid_redirect ( -- replicate (verbose)
        gid                 UUID NOT NULL, -- PK
        new_id              INTEGER NOT NULL, -- references artist.id
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class artist_gid_redirect(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    gid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    new_id = models.ForeignKey('artist')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Artist GID Redirect'

    class Meta:
        db_table = 'artist_gid_redirect'
