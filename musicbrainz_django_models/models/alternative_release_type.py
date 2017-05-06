"""
.. module:: alternative_release_type

PostreSQL Definition
--------------------

The :code:`alternative_release_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE alternative_release_type ( -- replicate
        id                  SERIAL, -- PK
        name                TEXT NOT NULL,
        parent              INTEGER, -- references alternative_release_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


def pre_save_alternative_release_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'Alternative Release Type Name "{}" is not one of: {}'.format(
                instance.name,
                ', '.join(sender.NAME_CHOICE_LIST)))


@python_2_unicode_compatible
class alternative_release_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: The name can be one of a range of values. This is not
        restricted in the SQL. In Django, this is implemented as a `choices`
        parameter to the `name` field, and a `pre_save` signal that performs
        the validation.
    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    TRANSLATION = 'Translation'
    OFFICIAL_TRANSLATION = 'Official Ttranslation'
    EXACTLY_AS_ON_COVER = 'Exactly as on cover'
    NAME_CHOICES = (
        (TRANSLATION, TRANSLATION),
        (OFFICIAL_TRANSLATION, OFFICIAL_TRANSLATION),
        (EXACTLY_AS_ON_COVER, EXACTLY_AS_ON_COVER),)
    NAME_CHOICE_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.TextField(choices=NAME_CHOICES)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'alternative_release_type'
        verbose_name_plural = 'Alternative Release Types'


models.signals.pre_save.connect(
    pre_save_alternative_release_type, sender=alternative_release_type)
