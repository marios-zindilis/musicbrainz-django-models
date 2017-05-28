"""
.. module:: autoeditor_election

The **Autoeditor Election** Model.

PostgreSQL Definition
---------------------

The :code:`autoeditor_election` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE autoeditor_election
    (
        id                  SERIAL,
        candidate           INTEGER NOT NULL, -- references editor.id
        proposer            INTEGER NOT NULL, -- references editor.id
        seconder_1          INTEGER, -- references editor.id
        seconder_2          INTEGER, -- references editor.id
        status              INTEGER NOT NULL DEFAULT 1
                                CHECK (status IN (1,2,3,4,5,6)),
                                -- 1 : has proposer
                                -- 2 : has seconder_1
                                -- 3 : has seconder_2 (voting open)
                                -- 4 : accepted!
                                -- 5 : rejected
                                -- 6 : cancelled (by proposer)
        yes_votes           INTEGER NOT NULL DEFAULT 0,
        no_votes            INTEGER NOT NULL DEFAULT 0,
        propose_time        TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
        open_time           TIMESTAMP WITH TIME ZONE,
        close_time          TIMESTAMP WITH TIME ZONE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


@python_2_unicode_compatible
class autoeditor_election(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.
    """

    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey('editor', related_name='autoeditor_election_candidates')
    proposer = models.ForeignKey('editor', related_name='autoeditor_election_proposers')
    seconder_1 = models.ForeignKey('editor', related_name='autoeditor_election_seconders_1')
    seconder_2 = models.ForeignKey('editor', related_name='autoeditor_election_seconders_2')
    status = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    yes_votes = models.IntegerField(default=0)
    no_votes = models.IntegerField(default=0)
    propose_time = models.DateTimeField(auto_now=True)
    open_time = models.DateTimeField(null=True)
    close_time = models.DateTimeField(null=True)

    def __str__(self):
        return 'Autoeditor Election'

    class Meta:
        db_table = 'autoeditor_election'
