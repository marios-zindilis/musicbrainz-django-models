"""
.. module:: alternative_track

The **Alternative Track** model.

PostgreSQL Definition
---------------------

The :code:`alternative_track` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE alternative_track ( -- replicate
        id                      SERIAL, -- PK
        name                    VARCHAR,
        artist_credit           INTEGER, -- references artist_credit.id
        ref_count               INTEGER NOT NULL DEFAULT 0
        CHECK (name != '' AND (name IS NOT NULL OR artist_credit IS NOT NULL))
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


def pre_save_alternative_track(sender, instance, **kwargs):
    if instance.name is None and instance.artist_credit is None:
        raise ValidationError('Either "name" or "artist_credit" must be set.')


@python_2_unicode_compatible
class alternative_track(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL. Also, while both the `name` and the `artist_credit` can be
        empty, both cannot be empty at the same time. This is implemented in
        Django with a `pre_save` signal.
    :param artist_credit: references :class:`.artist_credit`. Also see note
        on the `name` parameter.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    artist_credit = models.ForeignKey('artist_credit', null=True)
    ref_count = models.IntegerField(default=0)

    def __str__(self):
        if self.name:
            return self.name
        return str(self.artist_credit)

    class Meta:
        db_table = 'alternative_track'
        verbose_name_plural = 'Alternative Tracks'


models.signals.pre_save.connect(
    pre_save_alternative_track, sender=alternative_track)
