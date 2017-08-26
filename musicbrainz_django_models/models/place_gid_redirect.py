"""
.. module:: place_gid_redirect

The **Place Gid Redirect** Model.

PostgreSQL Definition
---------------------

The :code:`place_gid_redirect` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place_gid_redirect ( -- replicate (verbose)
        gid                 UUID NOT NULL, -- PK
        new_id              INTEGER NOT NULL, -- references place.id
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_gid_redirect import abstract__model_gid_redirect


@python_2_unicode_compatible
class place_gid_redirect(abstract__model_gid_redirect):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param new_id: References :class:`place`
    """

    new_id = models.ForeignKey('place')

    def __str__(self):
        return 'Place GID Redirect'

    class Meta:
        db_table = 'place_gid_redirect'
