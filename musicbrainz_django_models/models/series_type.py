"""
.. module:: series_type

The **Series Type** Model.

PostgreSQL Definition
---------------------

The :code:`series_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_type ( -- replicate (verbose)
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        entity_type         VARCHAR(50) NOT NULL,
        parent              INTEGER, -- references series_type.id
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
class series_type(abstract__model_type):
    RELEASE_GROUP = 'Release Group'
    RELEASE = 'Release'
    RECORDING = 'Recording'
    WORK = 'Work'
    CATALOGUE = 'Catalogue'
    EVENT = 'Event'
    TOUR = 'Tour'
    FESTIVAL = 'Festival'
    RUN = 'Run'
    NAME_CHOICES = (
        (RELEASE_GROUP, RELEASE_GROUP),
        (RELEASE, RELEASE),
        (RECORDING, RECORDING),
        (WORK, WORK),
        (CATALOGUE, CATALOGUE),
        (EVENT, EVENT),
        (TOUR, TOUR),
        (FESTIVAL, FESTIVAL),
        (RUN, RUN)
    )
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.CharField(max_length=255, choices=NAME_CHOICES)

    class Meta:
        db_table = 'series_type'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=series_type)
