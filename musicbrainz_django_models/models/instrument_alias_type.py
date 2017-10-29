"""
.. module:: instrument_alias_type

The **Instrument Alias Type** Model. Here's a complete table of values, from the
MusicBrainz database dump of 2017-07-22:

+----+-----------------+--------+-------------+-------------+--------------------------------------+
| id | name            | parent | child_order | description | gid                                  |
+====+=================+========+=============+=============+======================================+
|  1 | Instrument name |        |           0 |             | 2322fc94-fbf3-3c09-b23c-aa5ec8d14fcd |
+----+-----------------+--------+-------------+-------------+--------------------------------------+
|  2 | Search hint     |        |             |             | 7d5ef40f-4856-3000-8667-aa13b9db547d |
+----+-----------------+--------+-------------+-------------+--------------------------------------+

PostgreSQL Definition
---------------------

The :code:`instrument_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_alias_type ( -- replicate
        id                  SERIAL, -- PK,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references instrument_alias_type.id
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
class instrument_alias_type(abstract__model_alias_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    INSTRUMENT_NAME = 'Instrument name'
    SEARCH_HINT = 'Search hint'
    NAME_CHOICES = (
        (INSTRUMENT_NAME, INSTRUMENT_NAME),
        (SEARCH_HINT, SEARCH_HINT))
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.TextField(choices=NAME_CHOICES)

    class Meta:
        db_table = 'instrument_alias_type'


models.signals.pre_save.connect(pre_save_model_alias_type, sender=instrument_alias_type)
