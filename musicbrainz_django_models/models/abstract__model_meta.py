"""
.. module:: abstract__model_meta

This is an Abstract Django Model, meant to be subclassed by Models that store
Metadata in the same way, namely:

1. :class:`artist_meta`
2. :class:`event_meta`
3. :class:`label_meta`
4. :class:`recording_meta`
5. :class:`work_meta`

Those models are defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE <MODEL>_meta ( -- replicate
        id              INTEGER NOT NULL, -- PK, references <MODEL>.id CASCADE
        rating          SMALLINT CHECK (rating >= 0 AND rating <= 100),
        rating_count    INTEGER
    );

"""

from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


class abstract__model_meta(models.Model):

    RATING_MIN = 0
    RATING_MAX = 100

    rating = models.PositiveSmallIntegerField(
        null=True,
        validators=[MaxValueValidator(RATING_MAX)])
    rating_count = models.IntegerField(null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Validate that the value of `rating` is between 0 and 100.
        """
        if self.rating is not None and not self.RATING_MIN <= self.rating <= self.RATING_MAX:
            raise ValidationError('The rating is outside the range {} - {}'.format(
                self.RATING_MIN,
                self.RATING_MAX))
        super(abstract__model_meta, self).save(*args, **kwargs)
