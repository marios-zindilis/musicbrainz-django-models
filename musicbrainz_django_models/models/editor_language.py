"""
.. module:: editor_language

The **Editor Language** Model.

PostgreSQL Definition
---------------------

The :code:`editor_language` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TYPE FLUENCY AS ENUM ('basic', 'intermediate', 'advanced', 'native');

    CREATE TABLE editor_language (
        editor   INTEGER NOT NULL,  -- PK, references editor.id
        language INTEGER NOT NULL,  -- PK, references language.id
        fluency  FLUENCY NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


def pre_save_editor_language(sender, instance, **kwargs):
    if instance.fluency not in sender.FLUENCY_CHOICES_LIST:
        raise ValidationError('Fluency "{}" is not one of {}'.format(
            instance.fluency,
            ', '.join(sender.FLUENCY_CHOICES_LIST)))


@python_2_unicode_compatible
class editor_language(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`.editor`
    :param language: references :class:`.language`
    :param fluency: An `ENUM` type is used in the Postgres definition for this
        field. In Django, this can be implemented as a `CharField` with a list
        of choices.
    """

    BASIC = 'basic'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    NATIVE = 'native'
    FLUENCY_CHOICES = (
        (BASIC, BASIC),
        (INTERMEDIATE, INTERMEDIATE),
        (ADVANCED, ADVANCED),
        (NATIVE, NATIVE),)
    FLUENCY_CHOICES_LIST = [_[0] for _ in FLUENCY_CHOICES]

    editor = models.OneToOneField('editor', primary_key=True)
    language = models.OneToOneField('language')
    fluency = models.CharField(max_length=16, choices=FLUENCY_CHOICES)

    def __str__(self):
        return 'Editor Language'

    class Meta:
        db_table = 'editor_language'


models.signals.pre_save.connect(pre_save_editor_language, sender=editor_language)
