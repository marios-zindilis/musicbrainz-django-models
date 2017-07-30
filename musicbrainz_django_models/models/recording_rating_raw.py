"""
.. module:: recording_rating_raw

The **Recording Rating Raw** Model.

PostgreSQL Definition
---------------------

The :code:`recording_rating_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE recording_rating_raw
    (
        recording           INTEGER NOT NULL, -- PK, references recording.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        rating              SMALLINT NOT NULL CHECK (rating >= 0 AND rating <= 100)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


def pre_save_recording_rating_raw(sender, instance, **kwargs):
    if not sender.RATING_MIN <= instance.rating <= sender.RATING_MAX:
        raise ValidationError('Rating not in range {} - {}'.format(
            sender.RATING_MIN,
            sender.RATING_MAX))


@python_2_unicode_compatible
class recording_rating_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    RATING_MIN = 0
    RATING_MAX = 100

    recording = models.OneToOneField('recording', primary_key=True)
    editor = models.OneToOneField('editor')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(RATING_MAX)])

    def __str__(self):
        return 'Recording Rating Raw'

    class Meta:
        db_table = 'recording_rating_raw'


models.signals.pre_save.connect(pre_save_recording_rating_raw, sender=recording_rating_raw)
