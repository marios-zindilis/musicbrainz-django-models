"""
.. module:: link_text_attribute_type

The **Link Text Attribute Type** Model.

PostgreSQL Definition
---------------------

The :code:`link_text_attribute_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE link_text_attribute_type ( -- replicate
        attribute_type      INT NOT NULL -- PK, references link_attribute_type.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class link_text_attribute_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param attribute_type: references :class:`.link_attribute_type`
    """

    attribute_type = models.OneToOneField('link_attribute_type', primary_key=True)

    def __str__(self):
        return str(self.attribute_type)

    class Meta:
        db_table = 'link_text_attribute_type'
