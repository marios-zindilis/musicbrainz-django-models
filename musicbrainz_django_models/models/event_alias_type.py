"""
.. module:: event_alias_type

The **Event Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`event_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE event_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references event_alias_type.id
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
class event_alias_type(abstract__model_alias_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: This is restricted to the choices found in the
        MusicBrainz Server database dump.
    """

    EVENT_NAME = 'Event name'
    SEARCH_HINT = 'Search hint'
    NAME_CHOICES = (
        (EVENT_NAME, EVENT_NAME),
        (SEARCH_HINT, SEARCH_HINT))
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.TextField(choices=NAME_CHOICES)

    class Meta:
        db_table = 'event_alias_type'


models.signals.pre_save.connect(pre_save_model_alias_type, sender=event_alias_type)
