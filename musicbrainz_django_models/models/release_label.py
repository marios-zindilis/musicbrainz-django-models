"""
.. module:: release_label

The **Release Label** Model.

PostgreSQL Definition
---------------------

The :code:`release_label` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_label ( -- replicate (verbose)
        id                  SERIAL,
        release             INTEGER NOT NULL, -- references release.id
        label               INTEGER, -- references label.id
        catalog_number      VARCHAR(255),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class release_label(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release`.
    :param label: References :class:`label`.
    """

    id = models.AutoField(primary_key=True)
    release = models.ForeignKey('release')
    label = models.ForeignKey('label', null=True)
    catalog_number = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Release Label'

    class Meta:
        db_table = 'release_label'
