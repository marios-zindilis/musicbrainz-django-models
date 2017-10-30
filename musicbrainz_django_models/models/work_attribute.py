"""
.. module:: work_attribute

The **Work Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`work_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_attribute ( -- replicate (verbose)
        id                                  SERIAL,  -- PK
        work                                INTEGER NOT NULL, -- references work.id
        work_attribute_type                 INTEGER NOT NULL, -- references work_attribute_type.id
        work_attribute_type_allowed_value   INTEGER, -- references work_attribute_type_allowed_value.id
        work_attribute_text                 TEXT
        CHECK (
            (work_attribute_type_allowed_value IS NULL AND work_attribute_text IS NOT NULL)
            OR
            (work_attribute_type_allowed_value IS NOT NULL AND work_attribute_text IS NULL)
        )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class work_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`work`.
    """

    id = models.AutoField(primary_key=True)
    work = models.ForeignKey('work')
    work_attribute_type = models.ForeignKey('work_attribute_type')
    work_attribute_type_allowed_value = models.ForeignKey('work_attribute_type_allowed_value', null=True)
    work_attribute_text = models.TextField(null=True)

    def save(self, *args, **kwargs):
        # Both `work_attribute_type_allowed_value` and `work_attribute_text`
        # cannot be empty:
        if not any((self.work_attribute_type_allowed_value, self.work_attribute_text)):
            raise ValidationError(
                'work_attribute_type_allowed_value and work_attribute_text cannot both be empty.')
        # Both `work_attribute_type_allowed_value` and `work_attribute_text`
        # cannot both have value:
        if all((self.work_attribute_type_allowed_value, self.work_attribute_text)):
            raise ValidationError(
                'work_attribute_type_allowed_value and work_attribute_text cannot both have values.')
        super(work_attribute, self).save(*args, **kwargs)

    def __str__(self):
        return 'Work Attribute'

    class Meta:
        db_table = 'work_attribute'
