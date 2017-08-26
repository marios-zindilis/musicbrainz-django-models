"""
.. module:: url_gid_redirect

The **Url Gid Redirect** Model.

PostgreSQL Definition
---------------------

The :code:`url_gid_redirect` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE url_gid_redirect ( -- replicate
        gid                 UUID NOT NULL, -- PK
        new_id              INTEGER NOT NULL, -- references url.id
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_gid_redirect import abstract__model_gid_redirect


@python_2_unicode_compatible
class url_gid_redirect(abstract__model_gid_redirect):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param new_id: References :class:`url`
    """

    new_id = models.ForeignKey('url')

    def __str__(self):
        return 'Url GID Redirect'

    class Meta:
        db_table = 'url_gid_redirect'
