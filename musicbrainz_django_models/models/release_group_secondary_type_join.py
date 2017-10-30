"""
.. module:: release_group_secondary_type_join

The **Release Group Secondary Type Join** Model.

PostgreSQL Definition
---------------------

The :code:`release_group_secondary_type_join` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_group_secondary_type_join ( -- replicate (verbose)
        release_group INTEGER NOT NULL, -- PK, references release_group.id,
        secondary_type INTEGER NOT NULL, -- PK, references release_group_secondary_type.id
        created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_group_secondary_type_join(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release_group: References :class:`release_group`.
    :param secondary_type: References :class:`release_group_secondary_type`.
    """

    release_group = models.OneToOneField('release_group', primary_key=True)
    secondary_type = models.OneToOneField('release_group_secondary_type')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Release Group Secondary Type Join'

    class Meta:
        db_table = 'release_group_secondary_type_join'
