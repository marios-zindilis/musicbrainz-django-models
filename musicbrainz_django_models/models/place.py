"""
.. module:: place

The **Place** Model.

PostgreSQL Definition
---------------------

The :code:`place` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place ( -- replicate (verbose)
        id                  SERIAL, -- PK
        gid                 uuid NOT NULL,
        name                VARCHAR NOT NULL,
        type                INTEGER, -- references place_type.id
        address             VARCHAR NOT NULL DEFAULT '',
        area                INTEGER, -- references area.id
        coordinates         POINT,
        comment             VARCHAR(255) NOT NULL DEFAULT '',
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
          )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


def pre_save_place(sender, instance, **kwargs):
    instance.ended = (
        instance.end_date_year is not None or
        instance.end_date_month is not None or
        instance.end_date_day is not None)


@python_2_unicode_compatible
class place(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param coordinates: This field uses a `POINT` data type which is specific
        to Postgres for storing coordinates for points on a plane. An example
        is `(51.53192,-0.17835)` for Abbey Road Studions. In Django, this can
        be implemented as a `PointField` from the GeoDjango Model API. However
        this requires a database backend that supports that data type, and
        SQLite (that is used in this project) does not support it. It is
        possible to add it with Spatialite, but that is out of the scope of
        this effort. Therefore, a `CharField` is used here.
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
    type = models.ForeignKey('place_type')
    address = models.CharField(max_length=255)
    area = models.ForeignKey('area')
    coordinates = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'place'


models.signals.pre_save.connect(pre_save_place, sender=place)
