"""
.. module:: alternative_release_type

PostreSQL Definition
--------------------

The :code:`alternative_release_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE alternative_release_type ( -- replicate
        id                  SERIAL, -- PK
        name                TEXT NOT NULL,
        parent              INTEGER, -- references alternative_release_type.id
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
class alternative_release_type(abstract.model_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: The name can be one of a range of values. This is not
        restricted in the SQL. In Django, this is implemented as a `choices`
        parameter to the `name` field, and a `pre_save` signal that performs
        the validation.
    """

    TRANSLATION = 'Translation'
    OFFICIAL_TRANSLATION = 'Official Translation'
    EXACTLY_AS_ON_COVER = 'Exactly as on cover'
    NAME_CHOICES = (
        (TRANSLATION, TRANSLATION),
        (OFFICIAL_TRANSLATION, OFFICIAL_TRANSLATION),
        (EXACTLY_AS_ON_COVER, EXACTLY_AS_ON_COVER),)
    NAME_CHOICE_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.TextField(choices=NAME_CHOICES)

    class Meta:
        db_table = 'alternative_release_type'
        verbose_name_plural = 'Alternative Release Types'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=alternative_release_type)
