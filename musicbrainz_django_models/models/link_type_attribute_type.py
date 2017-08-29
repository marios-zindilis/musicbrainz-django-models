"""
.. module:: link_type_attribute_type

The **Link Type Attribute Type** Model.

PostgreSQL Definition
---------------------

The :code:`link_type_attribute_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE link_type_attribute_type ( -- replicate
        link_type           INTEGER NOT NULL, -- PK, references link_type.id
        attribute_type      INTEGER NOT NULL, -- PK, references link_attribute_type.id
        min                 SMALLINT,
        max                 SMALLINT,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class link_type_attribute_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param link_type: References :class:`link_type`.
    :param attribute_type: References :class:`link_attribute_type`.
    """

    link_type = models.OneToOneField('link_type', primary_key=True)
    attribute_type = models.OneToOneField('link_attribute_type')
    min = models.SmallIntegerField(null=True)
    max = models.SmallIntegerField(null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Link Type Attribute Type'

    class Meta:
        db_table = 'link_type_attribute_type'
