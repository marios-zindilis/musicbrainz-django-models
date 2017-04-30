"""
.. module:: release_group_primary_type

The **Release Group Primary Type** model. Release Groups have Primary and
Secondary types. Read more at the `Release Group Type on MusicBrainz`_.

.. _Release Group Type on MusicBrainz: https://musicbrainz.org/doc/Release_Group/Type

Here's a complete table of values, based on the MusicBrainz Server database
dump from 2017-04-19:

+----+-----------+--------+-------------+-------------+--------------------------------------+
| id | name      | parent | child_order | description | gid                                  |
+====+===========+========+=============+=============+======================================+
|  1 | Album     |        |           1 |             | f529b476-6e62-324f-b0aa-1f3e33d313fc |
+----+-----------+--------+-------------+-------------+--------------------------------------+
|  2 | Single    |        |           2 |             | d6038452-8ee0-3f68-affc-2de9a1ede0b9 |
+----+-----------+--------+-------------+-------------+--------------------------------------+
|  3 | EP        |        |           3 |             | 6d0c5bf6-7a33-3420-a519-44fc63eedebf |
+----+-----------+--------+-------------+-------------+--------------------------------------+
| 11 | Other     |        |          99 |             | 4fc3be2b-de1e-396b-a933-beb8f1607a22 |
+----+-----------+--------+-------------+-------------+--------------------------------------+
| 12 | Broadcast |        |           4 |             | 3b2e49e1-2875-37b8-9fa9-1f7cf3f49900 |
+----+-----------+--------+-------------+-------------+--------------------------------------+

PostreSQL Definition
--------------------

The :code:`release_group_primary_type` table is defined in the MusicBrainz
Server as:

.. code-block:: sql

    CREATE TABLE release_group_primary_type ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references release_group_primary_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
import uuid


def pre_save_release_group_primary_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'Release Group Primary Type "{}" is not one of: {}'.format(
                instance.name,
                ', '.join(sender.NAME_CHOICE_LIST)))


class release_group_primary_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of a range of values. This is not
        restricted in the SQL, but it is documented in
        `the Release Group Type documentation <https://musicbrainz.org/doc/Release_Group/Type>`_.
        In Django, this is implemented as a `choices` parameter to the `name`
        field, and a `pre_save` signal that performs the validation.
    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    ALBUM = 'Album'
    SINGLE = 'Single'
    EP = 'EP'
    OTHER = 'Other'
    BROADCAST = 'Broadcast'
    NAME_CHOICES = (
        (ALBUM, ALBUM),
        (SINGLE, SINGLE),
        (EP, EP),
        (OTHER, OTHER),
        (BROADCAST, BROADCAST),)
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
        db_table = 'release_group_primary_type'


models.signals.pre_save.connect(
    pre_save_release_group_primary_type, sender=release_group_primary_type)
