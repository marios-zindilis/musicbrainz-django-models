"""
.. module:: area

An **Area** is a country, region, city settlement, or the like. Areas were
imported in the MusicBrainz database from Wikidata once, and are not kept
automatically in sync.

Areas that can be used for filling in the Release country field of releases
are listed, by ID, in the :code:`country_area` table. 

    See the `Area Documentation on MusicBrainz`_.

.. _Area Documentation on MusicBrainz: https://musicbrainz.org/doc/Area

PostgreSQL Definition
---------------------

The :code:`area` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area ( -- replicate (verbose)
        id                  SERIAL, -- PK
        gid                 uuid NOT NULL,
        name                VARCHAR NOT NULL,
        type                INTEGER, -- references area_type.id
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >=0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        begin_date_year     SMALLINT,
        begin_date_month    SMALLINT,
        begin_date_day      SMALLINT,
        end_date_year       SMALLINT,
        end_date_month      SMALLINT,
        end_date_day        SMALLINT,
        ended               BOOLEAN NOT NULL DEFAULT FALSE
          CHECK (
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
        comment             VARCHAR(255) NOT NULL DEFAULT ''
    );

"""

from django.db import models
import uuid


def update_area_ended(sender, instance, **kwargs):
    instance.ended = instance.check_ended()


class area(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param type: references :class:`.area_type`
    :param smallint begin_date_year: You'd think this would be validated as a
        positive integer...
    :param smallint begin_date_month: ditto
    :param smallint begin_date_day: ditto
    :param smallint end_date_year: ditto
    :param smallint end_date_month: ditto
    :param smallint end_date_day: ditto
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        set this to `True` if any of the `end_*` fields has any value. This is
        implemented in Django with a `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    type = models.ForeignKey('area_type')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    ended = models.BooleanField(default=False)
    comment = models.CharField(max_length=255, default='')

    def check_ended(self):
        """
        Set `ended` to `True` if any of the `end_*` fields is populated.
        """
        return (
            self.end_date_year is not None or
            self.end_date_month is not None or
            self.end_date_day is not None)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'area'


models.signals.pre_save.connect(update_area_ended, sender=area)
