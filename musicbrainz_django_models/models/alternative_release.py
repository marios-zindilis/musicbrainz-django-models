"""
.. module:: alternative_release

The **Alternative Release** model.

PostgreSQL Definition
---------------------

The :code:`alternative_release` table is defined in the MusicBrainz server as:

.. code-block:: sql

    CREATE TABLE alternative_release ( -- replicate
        id                      SERIAL, -- PK
        gid                     UUID NOT NULL,
        release                 INTEGER NOT NULL, -- references release.id
        name                    VARCHAR,
        artist_credit           INTEGER, -- references artist_credit.id
        type                    INTEGER NOT NULL, -- references alternative_release_type.id
        language                INTEGER NOT NULL, -- references language.id
        script                  INTEGER NOT NULL, -- references script.id
        comment                 VARCHAR(255) NOT NULL DEFAULT ''
        CHECK (name != '')
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class alternative_release(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param str name: `max_length` is mandatory in Django models but not in
        PostgreSQL.
    """

    id = models.AutoField(primary_key=True)
    gid = models.UUIDField(default=uuid.uuid4)
    release = models.ForeignKey('release')
    name = models.CharField(max_length=255)
    artist_credit = models.ForeignKey('artist_credit', null=True)
    type = models.ForeignKey('alternative_release_type')
    language = models.ForeignKey('language')
    script = models.ForeignKey('script')
    comment = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'alternative_release'
        verbose_name_plural = 'Alternative Releases'
