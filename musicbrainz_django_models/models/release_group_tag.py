"""
.. module:: release_group_tag

The **Release Group Tag** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_tag ( -- replicate (verbose)
        release_group       INTEGER NOT NULL, -- PK, references release_group.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class release_group_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group: References :class:`release_group`
    """

    release_group = models.OneToOneField('release_group', primary_key=True)

    def __str__(self):
        return 'Release Group Tag'

    class Meta:
        db_table = 'release_group_tag'
