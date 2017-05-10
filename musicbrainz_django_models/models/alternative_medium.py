"""
.. module:: alternative_medium

The **Alternative Medium** model.

PostgreSQL Definition
---------------------

The :code:`alternative_medium` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE alternative_medium ( -- replicate
        id                      SERIAL, -- PK
        medium                  INTEGER NOT NULL, -- FK, references medium.id
        alternative_release     INTEGER NOT NULL, -- references alternative_release.id
        name                    VARCHAR
        CHECK (name != '')
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class alternative_medium(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: The maximum length is mandatory in Django but not in
        PostgreSQL.
    :param medium: references :class:`.medium`
    :param alternative_release: references :class:`.alternative_release`
    """

    id = models.AutoField(primary_key=True)
    medium = models.ForeignKey('medium')
    alternative_release = models.ForeignKey('alternative_release')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'alternative_medium'
        verbose_name_plural = 'Alternative Media'
