"""
.. module:: work_rating_raw

The **Work Rating Raw** Model.

PostgreSQL Definition
---------------------

The :code:`work_rating_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_rating_raw
    (
        work                INTEGER NOT NULL, -- PK, references work.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        rating              SMALLINT NOT NULL CHECK (rating >= 0 AND rating <= 100)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_rating_raw import abstract__model_rating_raw


@python_2_unicode_compatible
class work_rating_raw(abstract__model_rating_raw):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`work`.
    """

    work = models.OneToOneField('work', primary_key=True)

    def __str__(self):
        return 'Work Rating Raw'

    class Meta:
        db_table = 'work_rating_raw'
