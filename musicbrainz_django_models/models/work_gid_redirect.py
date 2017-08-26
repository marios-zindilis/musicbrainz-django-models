"""
.. module:: work_gid_redirect

The **Work Gid Redirect** Model.

PostgreSQL Definition
---------------------

The :code:`work_gid_redirect` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE work_gid_redirect ( -- replicate (verbose)
        gid                 UUID NOT NULL, -- PK
        new_id              INTEGER NOT NULL, -- references work.id
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_gid_redirect import abstract__model_gid_redirect


@python_2_unicode_compatible
class work_gid_redirect(abstract__model_gid_redirect):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param new_id: References :class:`work`.
    """

    new_id = models.ForeignKey('work')

    def __str__(self):
        return 'Work GID Redirect'

    class Meta:
        db_table = 'work_gid_redirect'
