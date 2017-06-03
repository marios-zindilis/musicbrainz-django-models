"""
.. module:: edit_artist

The **Edit Artist** Model.

PostgreSQL Definition
---------------------

The :code:`edit_artist` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_artist
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        artist              INTEGER NOT NULL, -- PK, references artist.id CASCADE
        status              SMALLINT NOT NULL -- materialized from edit.status
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


def pre_save_edit_artist(sender, instance, **kwargs):
    instance.status = instance.edit.status


@python_2_unicode_compatible
class edit_artist(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param artist: references :class:`.artist`
    :param status: This field's value reflects that of the referenced
        :class:`.edit` model, which in Django could be implemented as a model
        `@property` method, however that cannot be queried, so it is
        implemented here as a `SmallIntegerField`, populated with a `pre_save`
        signal.
    """

    edit = models.ForeignKey('edit')
    artist = models.ForeignKey('artist')
    status = models.SmallIntegerField()

    def __str__(self):
        return 'Edit Artist'

    class Meta:
        db_table = 'edit_artist'


models.signals.pre_save.connect(pre_save_edit_artist, sender=edit_artist)
