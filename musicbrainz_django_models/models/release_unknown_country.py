"""
.. module:: release_unknown_country

The **Release Unknown Country** Model.

PostgreSQL Definition
---------------------

The :code:`release_unknown_country` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_unknown_country ( -- replicate (verbose)
      release INTEGER NOT NULL,  -- PK, references release.id
      date_year SMALLINT,
      date_month SMALLINT,
      date_day SMALLINT
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_unknown_country(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release`.
    """

    release = models.OneToOneField('release', primary_key=True)
    date_year = models.SmallIntegerField(null=True)
    date_month = models.SmallIntegerField(null=True)
    date_day = models.SmallIntegerField(null=True)

    def __str__(self):
        return 'Release Unknown Country'

    class Meta:
        db_table = 'release_unknown_country'
