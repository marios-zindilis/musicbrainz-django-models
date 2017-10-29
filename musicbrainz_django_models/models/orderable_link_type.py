"""
.. module:: orderable_link_type

The **Orderable Link Type** Model.

PostgreSQL Definition
---------------------

The :code:`orderable_link_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE orderable_link_type ( -- replicate
        link_type           INTEGER NOT NULL, -- PK, references link_type.id
        direction           SMALLINT NOT NULL DEFAULT 1 CHECK (direction = 1 OR direction = 2)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


def pre_save_orderable_link_type(sender, instance, **kwargs):
    if not sender.DIRECTION_MIN <= instance.direction <= sender.DIRECTION_MAX:
        raise ValidationError('Direction not in range {} - {}'.format(
            sender.DIRECTION_MIN,
            sender.DIRECTION_MAX))


@python_2_unicode_compatible
class orderable_link_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param link_type: References :class:`link_type`.
    :param direction: In the PostgreSQL definition, this field has a check for
        its value, it can only be either 1 or 2. In Django, this restriction
        is implemented with a combination of Validator and a `pre_save`
        signal.
    """

    DIRECTION_MIN = 1
    DIRECTION_MAX = 2

    link_type = models.OneToOneField('link_type', primary_key=True)
    direction = models.SmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(DIRECTION_MIN),
            MaxValueValidator(DIRECTION_MAX)])

    def __str__(self):
        return 'Orderable Link Type'

    class Meta:
        db_table = 'orderable_link_type'


models.signals.pre_save.connect(pre_save_orderable_link_type, sender=orderable_link_type)
