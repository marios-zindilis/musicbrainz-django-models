"""
.. module:: alternative_medium_track

The **Alternative Medium Track** model.

PostgreSQL Definition
---------------------

The :code:`alternative_medium_track` table is defined in the MusicBrainz
server as:

.. code-block:: sql

    CREATE TABLE alternative_medium_track ( -- replicate
        alternative_medium      INTEGER NOT NULL, -- PK, references alternative_medium.id
        track                   INTEGER NOT NULL, -- PK, references track.id
        alternative_track       INTEGER NOT NULL -- references alternative_track.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class alternative_medium_track(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param alternative_medium: references :class:`.alternative_medium`
    :param track: references :class:`.track`
    :param alternative_track: references :class:`.alternative_track`
    """

    alternative_medium = models.ForeignKey('alternative_medium', primary_key=True)
    track = models.ForeignKey('track')
    alternative_track = models.ForeignKey('alternative_track')

    def __str__(self):
        return '{} {}'.format(str(self.alternative_medium), str(self.track))

    class Meta:
        db_table = 'alternative_medium_track'
        verbose_name_plural = 'Alterative Medium Tracks'
