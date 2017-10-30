"""
.. module:: release_country

The **Release Country** Model.

PostgreSQL Definition
---------------------

The :code:`release_country` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_country ( -- replicate (verbose)
      release INTEGER NOT NULL,  -- PK, references release.id
      country INTEGER NOT NULL,  -- PK, references country_area.area
      date_year SMALLINT,
      date_month SMALLINT,
      date_day SMALLINT
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_country(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release`.
    :param country: References :class:`country_area`
    """

    release = models.OneToOneField('release', primary_key=True)
    country = models.OneToOneField('country_area')
    date_year = models.SmallIntegerField(null=True)
    date_month = models.SmallIntegerField(null=True)
    date_day = models.SmallIntegerField(null=True)

    def __str__(self):
        return 'Release Country'

    class Meta:
        db_table = 'release_country'
