"""
.. module:: release_group_tag_raw

The **Release Group Tag Raw** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_tag_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_tag_raw
    (
        release_group       INTEGER NOT NULL, -- PK, references release_group.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        is_upvote           BOOLEAN NOT NULL DEFAULT TRUE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag_raw import abstract__model_tag_raw


@python_2_unicode_compatible
class release_group_tag_raw(abstract__model_tag_raw):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group: References :class:`release_group`.
    """

    release_group = models.OneToOneField('release_group', primary_key=True)

    def __str__(self):
        return 'Release Group Tag Raw'

    class Meta:
        db_table = 'release_group_tag_raw'
