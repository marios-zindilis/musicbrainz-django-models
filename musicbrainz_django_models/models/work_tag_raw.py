"""
.. module:: work_tag_raw

The **Work Tag Raw** Model.

PostgreSQL Definition
---------------------

The :code:`work_tag_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_tag_raw
    (
        work                INTEGER NOT NULL, -- PK, references work.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        is_upvote           BOOLEAN NOT NULL DEFAULT TRUE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class work_tag_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param work: References :class:`work`.
    """

    work = models.OneToOneField('work', primary_key=True)

    def __str__(self):
        return 'Work Tag Raw'

    class Meta:
        db_table = 'work_tag_raw'
