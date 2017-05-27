"""
.. module:: artist_meta

The **Artist Meta** Model.

PostgreSQL Definition
---------------------

The :code:`artist_meta` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_meta ( -- replicate
        id                  INTEGER NOT NULL, -- PK, references artist.id CASCADE
        rating              SMALLINT CHECK (rating >= 0 AND rating <= 100),
        rating_count        INTEGER
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


def pre_save_artist_meta(sender, instance, **kwargs):
    if (
        instance.rating is not None and
        not sender.RATING_MIN <= instance.rating <= sender.RATING_MAX
    ):
        raise ValidationError('The rating is outside the range {} - {}'.format(
            sender.RATING_MIN,
            sender.RATING_MAX))


@python_2_unicode_compatible
class artist_meta(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param int id: references :class:`.artist`. This is both a foreign and a
        primary key, best implemented in Django as a `OneToOneField`.
    :param int rating: This field has a check for its range of values. This is
        implemented with validators, and with a `pre_save` signal.
    """

    RATING_MIN = 0
    RATING_MAX = 100

    id = models.OneToOneField('artist', primary_key=True)
    rating = models.PositiveSmallIntegerField(
        null=True,
        validators=[MaxValueValidator(RATING_MAX)])
    rating_count = models.IntegerField(null=True)

    def __str__(self):
        return 'Artist Meta'

    class Meta:
        db_table = 'artist_meta'


models.signals.pre_save.connect(pre_save_artist_meta, sender=artist_meta)
