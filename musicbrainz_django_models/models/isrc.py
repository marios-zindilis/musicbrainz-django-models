"""
.. module:: isrc

The **ISRC** Model holds the International Standard Recording Code.

    See the `ISRC Documentation on MusicBrainz`_.
    See the `ISRC Wikipedia page`_.

.. _ISRC Documentation on MusicBrainz: https://musicbrainz.org/doc/ISRC
.. _ISRC Wikipedia page: https://en.wikipedia.org/wiki/International_Standard_Recording_Code

PostgreSQL Definition
---------------------

The :code:`isrc` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE isrc ( -- replicate (verbose)
        id                  SERIAL,
        recording           INTEGER NOT NULL, -- references recording.id
        isrc                CHAR(12) NOT NULL CHECK (isrc ~ E'^[A-Z]{2}[A-Z0-9]{3}[0-9]{7}$'),
        source              SMALLINT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator


def pre_save_isrc(sender, instance, **kwargs):
    import re
    if not re.match(sender.ISRC_REGEX, str(instance.isrc)):
        from django.core.exceptions import ValidationError
        raise ValidationError(RegexValidator.message)


@python_2_unicode_compatible
class isrc(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param recording: References :class:`.recording`
    :param str isrc: There is a regex-based check in SQL that is implemented
        in Django with a `RegexValidator` and a `pre_save` signal.
    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    """

    ISRC_REGEX = r'^[A-Z]{2}[A-Z0-9]{3}[0-9]{7}$'

    id = models.AutoField(primary_key=True)
    recording = models.ForeignKey('recording')
    isrc = models.CharField(max_length=12, validators=[RegexValidator(regex=ISRC_REGEX)])
    source = models.SmallIntegerField(null=True)
    edits_pending = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isrc

    class Meta:
        db_table = 'isrc'


models.signals.pre_save.connect(pre_save_isrc, sender=isrc)
