"""
.. module:: link_attribute

The **Link Attribute** Model.

PostgreSQL Definition
---------------------

The :code:`link_attribute` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE link_attribute ( -- replicate
        link                INTEGER NOT NULL, -- PK, references link.id
        attribute_type      INTEGER NOT NULL, -- PK, references link_attribute_type.id
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class link_attribute(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param link: References :class:`link`. This is both a Foreign Key to the
        :class:`link` model, as well as a Primary Key for `link_attribute`. In
        Django, this is best implemented as a `OneToOneField`.
    :param attribute_type: References :class:`link_attribute_type`.
    """

    link = models.OneToOneField('link', primary_key=True)
    attribute_type = models.OneToOneField('link_attribute_type')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Link Attribute'

    class Meta:
        db_table = 'link_attribute'
