"""
.. module:: label_isni

The **Label ISNI** Model. Holds the International Standard Name Identifier
for a Label. The ISNI is a 16-digit string. The first 15 characters are
numeric. The last character is a check character, and is either numeric or
the letter "X".

    See the `ISNI Documentation on MusicBrainz`_.
    See the `ISNI Wikipedia page`_.

.. _ISNI Documentation on MusicBrainz: https://musicbrainz.org/doc/ISNI
.. _ISNI Wikipedia page: https://en.wikipedia.org/wiki/International_Standard_Name_Identifier

Each Label can have multiple ISNIs. The ISNI page for a label looks like this:

    `http://www.isni.org/isni/0000000460211037`


PostgreSQL Definition
---------------------

The :code:`label_isni` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_isni ( -- replicate (verbose)
        label               INTEGER NOT NULL, -- PK, references label.id
        isni                CHAR(16) NOT NULL CHECK (isni ~ E'^\\d{15}[\\dX]$'), -- PK
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator


def pre_save_label_isni(sender, instance, **kwargs):
    import re
    if not re.match(sender.ISNI_REGEX, instance.isni):
        from django.core.exceptions import ValidationError
        raise ValidationError('Invalid value for the ISNI.')


@python_2_unicode_compatible
class label_isni(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param label: This field is interesting because it is both a Foreign Key
        to the Label model, as well the Primary Key for the Label ISNI
        model. In Django, this can be implemented as a `OneToOneField`.
    :param str isni: Both the `label` and the `isni` fields are primary keys
        in the SQL. In Django, there can only be 1 primary key per model.
        Therefore, the uniqueness required for a primary key is defined in
        this Django model field with a `unique` flag. Furthermore, there is a
        regex-based check in SQL. In Django, this can be implemented with a
        `RegexValidator`, but that is only applied in the frontend. For
        backend validation, a `pre_save` signal is used.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    """

    ISNI_REGEX = r'^\d{15}[\dX]$'

    label = models.OneToOneField('label', primary_key=True)
    isni = models.CharField(
        max_length=16,
        unique=True,
        validators=[
            MinLengthValidator(16),
            RegexValidator(regex=ISNI_REGEX)
        ]
    )
    edits_pending = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.isni)

    class Meta:
        db_table = 'label_isni'


models.signals.pre_save.connect(pre_save_label_isni, sender=label_isni)
