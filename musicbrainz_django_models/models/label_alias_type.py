"""
.. module:: label_alias_type

The **Label Alias Type** Model.

PostgreSQL Definition
---------------------

The :code:`label_alias_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_alias_type ( -- replicate
        id                  SERIAL,
        name                TEXT NOT NULL,
        parent              INTEGER, -- references label_alias_type.id
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
class label_alias_type(abstract__model_alias_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    """

    LABEL_NAME = 'Label name'
    SEARCH_HINT = 'Search hint'
    NAME_CHOICES = (
        (LABEL_NAME, LABEL_NAME),
        (SEARCH_HINT, SEARCH_HINT))
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.TextField(choices=NAME_CHOICES)

    class Meta:
        db_table = 'label_alias_type'


models.signals.pre_save.connect(pre_save_model_alias_type, sender=label_alias_type)
