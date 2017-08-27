"""
.. module:: work_tag

The **Work Tag** Model.

PostgreSQL Definition
---------------------

The :code:`work_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_tag ( -- replicate (verbose)
        work                INTEGER NOT NULL, -- PK, references work.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class work_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`work`.
    """

    work = models.OneToOneField('work', primary_key=True)

    def __str__(self):
        return 'Work Tag'

    class Meta:
        db_table = 'work_tag'
