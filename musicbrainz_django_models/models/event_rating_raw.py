"""
.. module:: event_rating_raw

The **Event Rating Raw** Model.

PostgreSQL Definition
---------------------

The :code:`event_rating_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_rating_raw (
        event               INTEGER NOT NULL, -- PK, references event.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        rating              SMALLINT NOT NULL CHECK (rating >= 0 AND rating <= 100)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


def pre_save_event_rating_raw(sender, instance, **kwargs):
    if not sender.RATING_MIN <= instance.rating <= sender.RATING_MAX:
        raise ValidationError('Rating not in range {} - {}'.format(
            sender.RATING_MIN,
            sender.RATING_MAX))


@python_2_unicode_compatible
class event_rating_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param event: references :class:`.event`
    :param editor: references :class:`.editor`
    :param int rating: This field has a check for its range of values. This is
        implemented with validators, and with a `pre_save` signal.
    """

    RATING_MIN = 0
    RATING_MAX = 100

    event = models.OneToOneField('event', primary_key=True)
    editor = models.OneToOneField('editor')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(RATING_MAX)])

    def __str__(self):
        return 'Event Rating Raw'

    class Meta:
        db_table = 'event_rating_raw'


models.signals.pre_save.connect(
    pre_save_event_rating_raw, sender=event_rating_raw)
