"""
.. module:: series_ordering_type

The **Series Ordering Type** Model.

PostgreSQL Definition
---------------------

The :code:`series_ordering_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE series_ordering_type ( -- replicate (verbose)
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references series_ordering_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_name_is_member_of_name_choices_list
from . import abstract


@python_2_unicode_compatible
class series_ordering_type(abstract.model_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of a range of values, not restricted
        in the SQL, but found in the MusicBrainz database dump.
    """

    AUTOMATIC = 'Automatic'
    MANUAL = 'Manual'
    NAME_CHOICES = (
        (AUTOMATIC, AUTOMATIC),
        (MANUAL, MANUAL))
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.CharField(max_length=255, choices=NAME_CHOICES)

    class Meta:
        db_table = 'series_ordering_type'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=series_ordering_type)
