"""
.. module:: artist_rating_raw

The **Artist Rating Raw** Model.

PostgreSQL Definition
---------------------

The :code:`artist_rating_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_rating_raw
    (
        artist              INTEGER NOT NULL, -- PK, references artist.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        rating              SMALLINT NOT NULL CHECK (rating >= 0 AND rating <= 100)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


def pre_save_artist_rating_raw(sender, instance, **kwargs):
    if not sender.RATING_MIN <= instance.rating <= sender.RATING_MAX:
        raise ValidationError('Rating not in range {} - {}'.format(
            sender.RATING_MIN,
            sender.RATING_MAX))


@python_2_unicode_compatible
class artist_rating_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    RATING_MIN = 0
    RATING_MAX = 100

    artist = models.OneToOneField('artist', primary_key=True)
    editor = models.OneToOneField('editor')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(RATING_MAX)])

    def __str__(self):
        return 'Artist Rating Raw'

    class Meta:
        db_table = 'artist_rating_raw'


models.signals.pre_save.connect(
    pre_save_artist_rating_raw, sender=artist_rating_raw)
