"""
.. module:: link_attribute_text_value

The **Link Attribute Text Value** Model.

PostgreSQL Definition
---------------------

The :code:`link_attribute_text_value` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE link_attribute_text_value ( -- replicate
        link                INT NOT NULL, -- PK, references link.id
        attribute_type      INT NOT NULL, -- PK, references link_text_attribute_type.attribute_type
        text_value          TEXT NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class link_attribute_text_value(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param link: References :class:`link`.
    :param attribute_type: References :class:`link_text_attribute_type`.
    """

    link = models.OneToOneField('link', primary_key=True)
    attribute_type = models.OneToOneField('link_text_attribute_type')
    text_value = models.TextField()

    def __str__(self):
        return 'Link Attribute Text Value'

    class Meta:
        db_table = 'link_attribute_text_value'
