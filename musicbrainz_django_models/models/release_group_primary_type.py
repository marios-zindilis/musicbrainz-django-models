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
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_type import abstract__model_type
from ..signals import pre_save_name_is_member_of_name_choices_list


@python_2_unicode_compatible
class release_group_primary_type(abstract__model_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of a range of values. This is not
        restricted in the SQL, but it is documented in
        `the Release Group Type documentation <https://musicbrainz.org/doc/Release_Group/Type>`_.
        In Django, this is implemented as a `choices` parameter to the `name`
        field, and a `pre_save` signal that performs the validation.
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
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.CharField(max_length=255, choices=NAME_CHOICES)

    class Meta:
        db_table = 'release_group_primary_type'
        verbose_name_plural = 'Release Group Primary Types'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=release_group_primary_type)
