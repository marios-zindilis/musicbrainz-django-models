"""
.. module:: release_group_rating_raw

The **Release Group Rating Raw** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_rating_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_rating_raw
    (
        release_group       INTEGER NOT NULL, -- PK, references release_group.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        rating              SMALLINT NOT NULL CHECK (rating >= 0 AND rating <= 100)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_rating_raw import abstract__model_rating_raw


@python_2_unicode_compatible
class release_group_rating_raw(abstract__model_rating_raw):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group: References :class:`release_group`.
    """

    release_group = models.OneToOneField('release_group', primary_key=True)

    def __str__(self):
        return 'Release Group Rating Raw'

    class Meta:
        db_table = 'release_group_rating_raw'
