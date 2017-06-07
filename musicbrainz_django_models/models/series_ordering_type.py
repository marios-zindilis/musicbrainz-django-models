"""
.. module:: series_ordering_type

The **Series Ordering Type** Model.

PostgreSQL Definition
---------------------

The :code:`series_ordering_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_ordering_type ( -- replicate (verbose)
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references series_ordering_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


def pre_save_series_ordering_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICES_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError('Name "{}" is not one of: {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICES_LIST)))


@python_2_unicode_compatible
class series_ordering_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    AUTOMATIC = 'Automatic'
    MANUAL = 'Manual'
    NAME_CHOICES = (
        (AUTOMATIC, AUTOMATIC),
        (MANUAL, MANUAL))
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    parent = models.ForeignKey('self')
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'series_ordering_type'


models.signals.pre_save.connect(pre_save_series_ordering_type, sender=series_ordering_type)
