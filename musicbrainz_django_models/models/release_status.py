"""
.. module:: release_status

The **Release Status** is one of:

1. Official
2. Promotion
3. Bootleg
4. Pseudo-Release

The Release Status is referenced by the Release model. Read more at the
`Release documentation on MusicBrainz`_.

.. _Release documentation on MusicBrainz: https://musicbrainz.org/doc/Release

PostreSQL Definition
--------------------

The :code:`release_status` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_status ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references release_status.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
import uuid


def pre_save_release_status(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'Release Status Name "{}" is not one of: {}'.format(
                instance.name,
                ', '.join(sender.NAME_CHOICE_LIST)))


class release_status(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of a range of values. This is not
        restricted in the SQL, but it is documented in
        `the Release documentation <https://musicbrainz.org/doc/Release>`_.
        In Django, this is implemented as a `choices` parameter to the `name`
        field, and a `pre_save` signal that performs the validation.
    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    OFFICIAL = 'Official'
    PROMOTION = 'Promotion'
    BOOTLEG = 'Bootleg'
    PSEUDO_RELEASE = 'Pseudo-Release'
    NAME_CHOICES = (
        (OFFICIAL, OFFICIAL),
        (PROMOTION, PROMOTION),
        (BOOTLEG, BOOTLEG),
        (PSEUDO_RELEASE, PSEUDO_RELEASE),)
    NAME_CHOICE_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'release_status'


models.signals.pre_save.connect(pre_save_release_status, sender=release_status)
