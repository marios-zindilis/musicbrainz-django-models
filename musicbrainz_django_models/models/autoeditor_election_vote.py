"""
.. module:: autoeditor_election_vote

The **Autoeditor Election Vote** Model.

PostgreSQL Definition
---------------------

The :code:`autoeditor_election_vote` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE autoeditor_election_vote
    (
        id                  SERIAL,
        autoeditor_election INTEGER NOT NULL, -- references autoeditor_election.id
        voter               INTEGER NOT NULL, -- references editor.id
        vote                INTEGER NOT NULL CHECK (vote IN (-1,0,1)),
        vote_time           TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


def pre_save_autoeditor_election_vote(sender, instance, **kwargs):
    if not sender.VOTE_MIN <= instance.vote <= sender.VOTE_MAX:
        raise ValidationError('Vote value not in range {} - {}'.format(
            sender.VOTE_MIN,
            sender.VOTE_MAX))


@python_2_unicode_compatible
class autoeditor_election_vote(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    VOTE_MIN = -1
    VOTE_MAX = 1

    id = models.AutoField(primary_key=True)
    autoeditor_election = models.ForeignKey('autoeditor_election')
    voter = models.ForeignKey('editor')
    vote = models.IntegerField(
        validators=[
            MinValueValidator(VOTE_MIN),
            MaxValueValidator(VOTE_MAX)])
    vote_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Autoeditor Election Vote'

    class Meta:
        db_table = 'autoeditor_election_vote'


models.signals.pre_save.connect(
    pre_save_autoeditor_election_vote, sender=autoeditor_election_vote)
