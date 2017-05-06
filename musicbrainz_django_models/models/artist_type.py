"""
.. module:: artist_type

The **Artist Type** Model. This can be one of:

1. Person
2. Group
3. Orchestra
4. Choir
5. Character
6. Other

Here's a complete table of values from the MusicBrainz database dump of
2017-04-19:

+----+-----------+--------+-------------+-------------+--------------------------------------+
| id | name      | parent | child_order | description | gid                                  |
+====+===========+========+=============+=============+======================================+
|  1 | Person    |        |           1 |             | b6e035f4-3ce9-331c-97df-83397230b0df |
+----+-----------+--------+-------------+-------------+--------------------------------------+
|  2 | Group     |        |           2 |             | e431f5f6-b5d2-343d-8b36-72607fffb74b |
+----+-----------+--------+-------------+-------------+--------------------------------------+
|  3 | Other     |        |          99 |             | ac897045-5043-3294-969b-187360e45d86 |
+----+-----------+--------+-------------+-------------+--------------------------------------+
|  4 | Character |        |           3 |             | 5c1375b0-f18d-3db7-a164-a49d7a63773f |
+----+-----------+--------+-------------+-------------+--------------------------------------+
|  5 | Orchestra |      2 |           0 |             | a0b36c92-3eb1-3839-a4f9-4799823f54a5 |
+----+-----------+--------+-------------+-------------+--------------------------------------+
|  6 | Choir     |      2 |           0 |             | 6124967d-7e3a-3eba-b642-c9a2ffb44d94 |
+----+-----------+--------+-------------+-------------+--------------------------------------+

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
from django.utils.encoding import python_2_unicode_compatible
import uuid


def validate_artist_type_name_choice(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError('Artist Type "{}" is not one of: {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICE_LIST)))


@python_2_unicode_compatible
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
        (OTHER, OTHER),
    )
    NAME_CHOICE_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist_type'
        verbose_name_plural = 'Artist Types'


models.signals.pre_save.connect(
    validate_artist_type_name_choice, sender=artist_type)
