"""
.. module:: release_group_secondary_type

The **Release Group Secondary Type** model. Release Groups have Primary and
Secondary types. Read more at the `Release Group Type on MusicBrainz`_.

.. _Release Group Type on MusicBrainz: https://musicbrainz.org/doc/Release_Group/Type

Here's a complete table of values, based on the MusicBrainz Server database
dump from 2017-04-19:

+----+----------------+--------+-------------+-------------+--------------------------------------+
| id | name           | parent | child_order | description | gid                                  |
+====+================+========+=============+=============+======================================+
|  1 | Compilation    |        |           0 |             | dd2a21e1-0c00-3729-a7a0-de60b84eb5d1 |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  2 | Soundtrack     |        |           0 |             | 22a628ad-c082-3c4f-b1b6-d41665107b88 |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  3 | Spokenword     |        |           0 |             | 66b8a13e-43ff-3ac0-ac6c-73659d3817c6 |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  4 | Interview      |        |           0 |             | 12af3f5e-ce2a-3941-8b93-d482884031e5 |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  5 | Audiobook      |        |           0 |             | 499a387e-6195-333e-91c0-9592bfec535e |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  6 | Live           |        |           0 |             | 6fd474e2-6b58-3102-9d17-d6f7eb7da0a0 |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  7 | Remix          |        |           0 |             | 0c60f497-ff81-3818-befd-abfc84a4858b |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  8 | DJ-mix         |        |           0 |             | 0d47f47a-3fe5-3d69-ac9d-d566c23968bf |
+----+----------------+--------+-------------+-------------+--------------------------------------+
|  9 | Mixtape/Street |        |           0 |             | 15c1b1f5-d893-3375-a1db-e180c5ae15ed |
+----+----------------+--------+-------------+-------------+--------------------------------------+
| 10 | Demo           |        |           0 |             | 81598169-0d6c-3bce-b4be-866fa658eda3 |
+----+----------------+--------+-------------+-------------+--------------------------------------+

PostreSQL Definition
--------------------

The :code:`release_group_secondary_type` table is defined in the MusicBrainz
Server as:

.. code-block:: sql

    CREATE TABLE release_group_secondary_type ( -- replicate
        id                  SERIAL, -- PK
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references release_group_secondary_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
import uuid


def pre_save_release_group_secondary_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'Release Group Secondary Type "{}" is not one of: {}'.format(
                instance.name,
                ', '.join(sender.NAME_CHOICE_LIST)))


class release_group_secondary_type(models.Model):
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

    COMPILATION = 'Compilation'
    SOUNDTRACK = 'Soundtrack'
    SPOKENWORD = 'Spokenword'
    INTERVIEW = 'Interview'
    AUDIOBOOK = 'Audiobook'
    LIVE = 'Live'
    REMIX = 'Remix'
    DJ_MIX = 'DJ-mix'
    MIXTAPE_STREET = 'Mixtape/Street'
    DEMO = 'Demo'
    NAME_CHOICES = (
        (COMPILATION, COMPILATION),
        (SOUNDTRACK, SOUNDTRACK),
        (SPOKENWORD, SPOKENWORD),
        (INTERVIEW, INTERVIEW),
        (AUDIOBOOK, AUDIOBOOK),
        (LIVE, LIVE),
        (REMIX, REMIX),
        (DJ_MIX, DJ_MIX),
        (MIXTAPE_STREET, MIXTAPE_STREET),
        (DEMO, DEMO),)
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
        db_table = 'release_group_secondary_type'


models.signals.pre_save.connect(
    pre_save_release_group_secondary_type, sender=release_group_secondary_type)
