"""
.. module:: work_language

The **Work Language** Model.

PostgreSQL Definition
---------------------

The :code:`work_language` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_language ( -- replicate (verbose)
        work                INTEGER NOT NULL, -- PK, references work.id
        language            INTEGER NOT NULL, -- PK, references language.id
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class work_language(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`work`.
    """

    work = models.OneToOneField('work', primary_key=True)
    language = models.OneToOneField('language')
    edits_pending = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Work Language'

    class Meta:
        db_table = 'work_language'
