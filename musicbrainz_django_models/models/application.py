"""
.. module:: application

The **application** Model.

PostgreSQL Definition
---------------------

The :code:`application` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE application
    (
        id                  SERIAL,
        owner               INTEGER NOT NULL, -- references editor.id
        name                TEXT NOT NULL,
        oauth_id            TEXT NOT NULL,
        oauth_secret        TEXT NOT NULL,
        oauth_redirect_uri  TEXT
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class application(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param owner: references :class:`.editor`
    """

    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('editor')
    name = models.TextField()
    oauth_id = models.TextField()
    oauth_secret = models.TextField()
    oauth_redirect_url = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'application'
