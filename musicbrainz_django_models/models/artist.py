"""
.. module:: artist

An **Artist** is generally a musician, group of musicians, or other music
professional (like a producer or engineer). Occasionally, it can also be a
non-musical person (like a photographer, an illustrator, or a poet whose
writings are set to music), or even a fictional character. For some other
special cases, there are special purpose artists.

    See the `Artist Documentation on MusicBrainz`_.

.. _Artist Documentation on MusicBrainz: https://musicbrainz.org/doc/Artist

PostgreSQL Definition
---------------------

The :code:`artist` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        sort_name           VARCHAR NOT NULL,
        begin_date_year     SMALLINT,
        begin_date_month    SMALLINT,
        begin_date_day      SMALLINT,
        end_date_year       SMALLINT,
        end_date_month      SMALLINT,
        end_date_day        SMALLINT,
        type                INTEGER, -- references artist_type.id
        area                INTEGER, -- references area.id
        gender              INTEGER, -- references gender.id
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        ended               BOOLEAN NOT NULL DEFAULT FALSE
          CONSTRAINT artist_ended_check CHECK (
            (
              -- If any end date fields are not null, then ended must be true
              (end_date_year IS NOT NULL OR
               end_date_month IS NOT NULL OR
               end_date_day IS NOT NULL) AND
              ended = TRUE
            ) OR (
              -- Otherwise, all end date fields must be null
              (end_date_year IS NULL AND
               end_date_month IS NULL AND
               end_date_day IS NULL)
            )
          ),
        begin_area          INTEGER, -- references area.id
        end_area            INTEGER -- references area.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


def update_artist_ended(sender, instance, **kwargs):
    instance.ended = instance.check_ended()


@python_2_unicode_compatible
class artist(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param str sort_name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param smallint begin_date_month: You'd think this would be validated as a
        range of 1-12 or similar...
    :param smallint end_date_month: ditto
    :param smallint begin_date_day: You'd think this would be validated as a
        range of 1-31 or similar...
    :param smallint end_date_day: ditto
    :param area: The `artist` model has 3 `ForeignKey` relationships to the
        `area` model. Django requires that at least 2 of them have a
        `related_name` defined.
    :param begin_area: ditto
    :param end_area: ditto
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        set this to `True` if any of the `end_*` fields has any value. This is
        implemented in Django with a `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    sort_name = models.CharField(max_length=255)
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    type = models.ForeignKey('artist_type', null=True)
    area = models.ForeignKey('area', null=True, related_name='artists')
    gender = models.ForeignKey('gender', null=True)
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    ended = models.BooleanField(default=False)
    begin_area = models.ForeignKey(
        'area',
        null=True,
        related_name='artists_begun')
    end_area = models.ForeignKey(
        'area',
        null=True,
        related_name='artists_ended')

    def check_ended(self):
        """
        Set `ended` to `True` if any of the `end_date_*` fields is populated.
        """
        return (
            self.end_date_year is not None or
            self.end_date_month is not None or
            self.end_date_day is not None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist'


models.signals.pre_save.connect(update_artist_ended, sender=artist)
