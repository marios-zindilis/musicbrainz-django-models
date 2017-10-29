"""
.. module:: place_alias_type

The **Place Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`place_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references place_alias_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_alias_type import abstract__model_alias_type
from ..signals import pre_save_model_alias_type


@python_2_unicode_compatible
class place_alias_type(abstract__model_alias_type):
    SEARCH_HINT = 'Search hint'
    NAME_CHOICES = (
        (SEARCH_HINT, SEARCH_HINT),)
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.TextField(choices=NAME_CHOICES)

    class Meta:
        db_table = 'place_alias_type'


models.signals.pre_save.connect(pre_save_model_alias_type, sender=place_alias_type)
