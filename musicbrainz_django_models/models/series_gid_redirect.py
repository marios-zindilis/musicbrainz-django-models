"""
.. module:: series_gid_redirect

The **Series Gid Redirect** Model.

PostgreSQL Definition
---------------------

The :code:`series_gid_redirect` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_gid_redirect ( -- replicate (verbose)
        gid                 UUID NOT NULL, -- PK
        new_id              INTEGER NOT NULL, -- references series.id
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_gid_redirect import abstract__model_gid_redirect


@python_2_unicode_compatible
class series_gid_redirect(abstract__model_gid_redirect):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param new_id: References :class:`series`.
    """

    new_id = models.ForeignKey('series')

    def __str__(self):
        return 'Series GID Redirect'

    class Meta:
        db_table = 'series_gid_redirect'
