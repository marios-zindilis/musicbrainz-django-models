"""
.. module:: edit_url

The **Edit Url** Model.

PostgreSQL Definition
---------------------

The :code:`edit_url` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_url
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        url                 INTEGER NOT NULL  -- PK, references url.id CASCADE
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_url(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param edit: references :class:`.edit`
    :param url: references :class:`.url`
    """

    edit = models.OneToOneField('edit', primary_key=True)
    url = models.OneToOneField('url')

    def __str__(self):
        return 'Edit URL'

    class Meta:
        db_table = 'edit_url'
