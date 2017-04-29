"""
.. module:: language

The **Language** model.

PostgreSQL Definition
---------------------

The :code:`language` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE language ( -- replicate
        id                  SERIAL,
        iso_code_2t         CHAR(3), -- ISO 639-2 (T)
        iso_code_2b         CHAR(3), -- ISO 639-2 (B)
        iso_code_1          CHAR(2), -- ISO 639
        name                VARCHAR(100) NOT NULL,
        frequency           INTEGER NOT NULL DEFAULT 0,
        iso_code_3          CHAR(3)  -- ISO 639-3
    );

    ALTER TABLE language
          ADD CONSTRAINT iso_code_check
          CHECK (iso_code_2t IS NOT NULL OR iso_code_3  IS NOT NULL);

"""

from django.db import models


def pre_save_language(sender, instance, **kwagrs):
    if not instance.iso_code_2t and not instance.iso_code_3:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'Either iso_code_2t or iso_code_3 must be defined')


class language(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param iso_code_2t: Either this parameter, or :code:`iso_code_3` must have
        a value, according to the `check` in the PostgreSQL definition. In
        Django, this is validated with a `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    iso_code_2t = models.CharField(
        max_length=3, null=True, help_text='ISO 639-2 (T)')
    iso_code_2b = models.CharField(
        max_length=3, null=True, help_text='ISO 639-2 (B)')
    iso_code_1 = models.CharField(max_length=2, null=True, help_text='ISO 639')
    name = models.CharField(max_length=100)
    frequency = models.IntegerField(default=0)
    iso_code_3 = models.CharField(
        max_length=3, null=True, help_text='ISO 639-3')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'language'


models.signals.pre_save.connect(pre_save_language, sender=language)
