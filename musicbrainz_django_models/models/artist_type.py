"""
.. module:: artist_type

The **Artist Type** Model. This can be one of:

1. Person
2. Group
3. Orchestra
4. Choir
5. Character
6. Other

    See the `Artist Documentation on MusicBrainz`_.

.. _Artist Documentation on MusicBrainz: https://musicbrainz.org/doc/Artist

PostgreSQL Definition
---------------------

The :code:`artist_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_type ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references artist_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL 
    );

"""

from django.db import models
import uuid


def validate_artist_type_name_choice(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError('Artist Type "{}" is not one of: {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICE_LIST)))


class artist_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: The name can have one of the following values: "Person",
        "Group", "Orchestra", "Choir", "Character" or "Other". This range of
        values is not restricted in the SQL definition, but it is documented
        in `the Artist documentation <https://musicbrainz.org/doc/Artist>`_.
        In Django, this is implemented as a `choices` parameter to the `name`
        field, and as a `pre_save` signal that performs the validation.
    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    PERSON = 'Person'
    GROUP = 'Group'
    ORCHESTRA = 'Orchestra'
    CHOIR = 'Choir'
    CHARACTER = 'Character'
    OTHER = 'Other'
    NAME_CHOICES = (
        (PERSON, PERSON),
        (GROUP, GROUP),
        (ORCHESTRA, ORCHESTRA),
        (CHOIR, CHOIR),
        (CHARACTER, CHARACTER),
        (OTHER,OTHER),
    )
    NAME_CHOICE_LIST = [choice[0] for choice in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist_type'


models.signals.pre_save.connect(
    validate_artist_type_name_choice, sender=artist_type)
