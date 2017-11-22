"""
.. module:: artist_alias_type

The **Artist Alias Type** Model. Here's a complete table of values, from the
MusicBrainz database dump of 2017-04-19:

+----+-------------+--------+-------------+-------------+--------------------------------------+
| id | name        | parent | child_order | description | gid                                  |
+====+=============+========+=============+=============+======================================+
|  1 | Artist name |        |           0 |             | 894afba6-2816-3c24-8072-eadb66bd04bc |
+----+-------------+--------+-------------+-------------+--------------------------------------+
|  2 | Legal name  |        |           0 |             | d4dcd0c0-b341-3612-a332-c0ce797b25cf |
+----+-------------+--------+-------------+-------------+--------------------------------------+
|  3 | Search hint |        |           0 |             | 1937e404-b981-3cb7-8151-4c86ebfc8d8e |
+----+-------------+--------+-------------+-------------+--------------------------------------+

    See the `Aliases Documentation on MusicBrainz`_.

.. _Aliases Documentation on MusicBrainz: https://musicbrainz.org/doc/Aliases

PostgreSQL Definition
---------------------

The :code:`artist_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE artist_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references artist_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from . import abstract
from ..signals import pre_save_name_is_member_of_name_choices_list


@python_2_unicode_compatible
class artist_alias_type(abstract.model_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: This field is not restricted to a range of values in the
        SQL definition. From the database dumps it is apparent that there are
        3 possible values: "Artist name", "Legal name" and "Search hint". This
        is implemented in Django with a `choices` parameter to the `name`
        field, as well as with a `pre_save` signal for validation.
    """

    ARTIST_NAME = 'Artist name'
    LEGAL_NAME = 'Legal name'
    SEARCH_HINT = 'Search hint'
    NAME_CHOICES = (
        (ARTIST_NAME, ARTIST_NAME),
        (LEGAL_NAME, LEGAL_NAME),
        (SEARCH_HINT, SEARCH_HINT),
    )
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    # Override the `name` attribute of `abstract__model_alias_type` to add choices:
    name = models.TextField(choices=NAME_CHOICES)

    class Meta:
        db_table = 'artist_alias_type'
        verbose_name_plural = 'Artist Alias Types'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=artist_alias_type)
