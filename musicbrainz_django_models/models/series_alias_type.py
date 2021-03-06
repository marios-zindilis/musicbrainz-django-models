"""
.. module:: series_alias_type

The **Series Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`series_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_alias_type ( -- replicate (verbose)
        id                  SERIAL, -- PK
        name                TEXT NOT NULL,
        parent              INTEGER, -- references series_alias_type.id
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
class series_alias_type(abstract.model_type):

    SEARCH_HINT = 'Search hint'
    NAME_CHOICES = (
        (SEARCH_HINT, SEARCH_HINT),)
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.TextField(choices=NAME_CHOICES)

    class Meta:
        db_table = 'series_alias_type'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=series_alias_type)
