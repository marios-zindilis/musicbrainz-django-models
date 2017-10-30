"""
.. module:: abstract__model_rating_raw

This is an Abstract Django Model meant to be subclassed by models that store
ratings in a similar manner, namely:

1.  :class:`artist_rating_raw`
2.  :class:`event_rating_raw`
3.  :class:`label_rating_raw`
4.  :class:`recording_rating_raw`
5.  :class:`release_group_rating_raw`
6.  :class:`work_rating_raw`

Those models are defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_rating_raw
    (
        <MODEL>     INTEGER NOT NULL, -- PK, references <MODEL>.id
        editor      INTEGER NOT NULL, -- PK, references editor.id
        rating      SMALLINT NOT NULL CHECK (rating >= 0 AND rating <= 100)
    );

"""

from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


class abstract__model_rating_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: References :class:`editor`.
    :param rating: In the PostgreSQL definition, a check verifies that the
        value of `rating` is between 0 and 100. In Django, this is implemented
        with a pair of validators for front-end verification, and with
        overriding `save()` for back-end verification.
    """

    RATING_MIN = 0
    RATING_MAX = 100

    editor = models.OneToOneField('editor')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(RATING_MIN),
            MaxValueValidator(RATING_MAX)])

    def save(self, *args, **kwargs):
        if not self.RATING_MIN <= self.rating <= self.RATING_MAX:
            raise ValidationError('Rating not in range {} - {}'.format(
                self.RATING_MIN, self.RATING_MAX))
        super(abstract__model_rating_raw, self).save(*args, **kwargs)

    class Meta:
        abstract = True
