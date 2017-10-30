"""
.. module:: tag_relation

The **Tag Relation** Model.

PostgreSQL Definition
---------------------

The :code:`tag_relation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE tag_relation
    (
        tag1                INTEGER NOT NULL, -- PK, references tag.id
        tag2                INTEGER NOT NULL, -- PK, references tag.id
        weight              INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        CHECK (tag1 < tag2)
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class tag_relation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    In the PostgreSQL definition of the table, there is a check that verifies
    that `tag1 < tag2`. This is probably meant to assert that the combination
    of `tag1` and `tag2` is unique. In Django, this can be implemented with
    the `unique_together` Meta option. Even better, in Django this table could
    be the `through` table of a Many-To-Many field in the `tag` model.

    :param tag1: References :class:`tag`.
    :param tag2: References :class:`tag`.
    """

    tag1 = models.OneToOneField('tag', primary_key=True, related_name='related_tags2')
    tag2 = models.OneToOneField('tag', related_name='related_tags1')
    weight = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Tag Relation'

    class Meta:
        db_table = 'tag_relation'
        unique_together = ('tag1', 'tag2')
