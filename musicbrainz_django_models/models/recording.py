"""
.. module:: recording

The **Release** model. Read more at the
`Recording documentation on MusicBrainz`_.

.. _Recording documentation on MusicBrainz: https://musicbrainz.org/doc/Recording

PostgreSQL Definition
---------------------

The :code:`recording` table is defined in the MusicBrainz server as:

.. code-block:: sql

    CREATE TABLE recording ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        artist_credit       INTEGER NOT NULL, -- references artist_credit.id
        length              INTEGER CHECK (length IS NULL OR length > 0),
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        video               BOOLEAN NOT NULL DEFAULT FALSE
    );

"""

from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import uuid


def pre_save_recording(sender, instance, **kwargs):
    if instance.length is not None and instance.length < 1:
        raise ValidationError('The Recording Length cannot be less that 1')


class recording(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    :param int length: The MusicBrainz Server uses a PostgreSQL `check` to
        validate that this field is either empty or contains a value larger
        than 0. In Django, this is implemented with a MinValueValidator and
        with a `pre_save` signal.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    artist_credit = models.ForeignKey('artist_credit')
    length = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1)])
    comment = models.CharField(max_length=255, default='')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    video = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'recording'


models.signals.pre_save.connect(pre_save_recording, sender=recording)
