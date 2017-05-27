"""
.. module:: area_tag_raw

The **Area Tag Raw** Model.

PostgreSQL Definition
---------------------

The :code:`area_tag_raw` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_tag_raw (
        area                INTEGER NOT NULL, -- PK, references area.id
        editor              INTEGER NOT NULL, -- PK, references editor.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        is_upvote           BOOLEAN NOT NULL DEFAULT TRUE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class area_tag_raw(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    The `area`, `editor` and `tag` parameters are all both foreign keys and
        primary keys. In Django, there can only be 1 primary key per model. The
        uniqueness required for a primary key is implemented as
        `OneToOneField`.

    :param area: references :class:`.area`
    :param editor: references :class:`.editor`
    :param tag: references :class:`.tag`
    """

    area = models.OneToOneField('area', primary_key=True)
    editor = models.OneToOneField('editor')
    tag = models.OneToOneField('tag')
    is_upvote = models.BooleanField(default=True)

    def __str__(self):
        return 'Area Tag Raw'

    class Meta:
        db_table = 'area_tag_raw'
