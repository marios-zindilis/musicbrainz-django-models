"""
.. module:: iswc

The **ISWC** Model holds the International Standard Musical Work Code.

    See the `ISWC Documentation on MusicBrainz`_.
    See the `ISWC Wikipedia page`_.

.. _ISWC Documentation on MusicBrainz: https://wiki.musicbrainz.org/ISWC
.. _ISWC Wikipedia page: https://en.wikipedia.org/wiki/International_Standard_Musical_Work_Code

PostgreSQL Definition
---------------------

The :code:`iswc` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE iswc ( -- replicate (verbose)
        id SERIAL NOT NULL,
        work INTEGER NOT NULL, -- references work.id
        iswc CHARACTER(15) CHECK (iswc ~ E'^T-?\\d{3}.?\\d{3}.?\\d{3}[-.]?\\d$'),
        source SMALLINT,
        edits_pending INTEGER NOT NULL DEFAULT 0,
        created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator


def pre_save_iswc(sender, instance, **kwargs):
    import re
    if not re.match(sender.ISWC_REGEX, str(instance.iswc)):
        from django.core.exceptions import ValidationError
        raise ValidationError(RegexValidator.message)


@python_2_unicode_compatible
class iswc(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`.work`.
    :param str iswc: There is a regex-based check in SQL that is implemented
        in Django with a `RegexValidator` and a `pre_save` signal.
    """

    ISWC_REGEX = r'^T-?\d{3}.?\d{3}.?\d{3}[-.]?\d$'

    id = models.AutoField(primary_key=True)
    work = models.ForeignKey('work')
    iswc = models.CharField(max_length=15, validators=[RegexValidator(regex=ISWC_REGEX)])
    source = models.SmallIntegerField(null=True)
    edits_pending = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.iswc

    class Meta:
        db_table = 'iswc'


models.signals.pre_save.connect(pre_save_iswc, sender=iswc)
