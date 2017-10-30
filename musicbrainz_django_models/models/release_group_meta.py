"""
.. module:: release_group_meta

The **Release Group Meta** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_meta` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_meta ( -- replicate
        id                  INTEGER NOT NULL, -- PK, references release_group.id CASCADE
        release_count       INTEGER NOT NULL DEFAULT 0,
        first_release_date_year   SMALLINT,
        first_release_date_month  SMALLINT,
        first_release_date_day    SMALLINT,
        rating              SMALLINT CHECK (rating >= 0 AND rating <= 100),
        rating_count        INTEGER
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class release_group_meta(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param id: References :class:`release_group`.
    """

    RATING_MIN = 0
    RATING_MAX = 100

    id = models.OneToOneField('release_group', primary_key=True)
    release_count = models.IntegerField(default=0)
    first_release_date_year = models.SmallIntegerField(null=True)
    first_release_date_month = models.SmallIntegerField(null=True)
    first_release_date_day = models.SmallIntegerField(null=True)
    rating = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(RATING_MIN),
            MaxValueValidator(RATING_MAX)])

    def save(self, *args, **kwargs):
        if self.rating:
            if not self.RATING_MIN <= self.rating <= self.RATING_MAX:
                raise ValidationError('Rating not in range {} - {}'.format(
                    self.RATING_MIN, self.RATING_MAX))
        super(release_group_meta, self).save(*args, **kwargs)

    def __str__(self):
        return 'Release Group Meta'

    class Meta:
        db_table = 'release_group_meta'
