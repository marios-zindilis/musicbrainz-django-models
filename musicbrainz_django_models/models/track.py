"""
.. module:: track

The **Track** model.

PostgreSQL Definition
---------------------

The :code:`track` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE track ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        recording           INTEGER NOT NULL, -- references recording.id
        medium              INTEGER NOT NULL, -- references medium.id
        position            INTEGER NOT NULL,
        number              TEXT NOT NULL,
        name                VARCHAR NOT NULL,
        artist_credit       INTEGER NOT NULL, -- references artist_credit.id
        length              INTEGER CHECK (length IS NULL OR length > 0),
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        is_data_track       BOOLEAN NOT NULL DEFAULT FALSE
    );

"""

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils.encoding import python_2_unicode_compatible
import uuid


def pre_save_track(sender, instance, **kwargs):
    if instance.length is not None and instance.length < 1:
        raise ValidationError('The Recording Length cannot be less that 1')


@python_2_unicode_compatible
class track(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param id: Auto-Incrementing Integer Primary Key
    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param recording: references :class:`.recording`
    :param medium: references :class:`.medium`
    :param artist_credit: references :class:`.artist_credit`
    :param int length: The MusicBrainz Server uses a PostgreSQL `check` to
        validate that this field is either empty or contains a value larger
        than 0. In Django, this is implemented with a MinValueValidator and
        with a `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    recording = models.ForeignKey('recording')
    medium = models.ForeignKey('medium')
    position = models.IntegerField()
    name = models.CharField(max_length=255)
    artist_credit = models.ForeignKey('artist_credit')
    length = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1)])
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    is_data_track = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'track'


models.signals.pre_save.connect(pre_save_track, sender=track)
