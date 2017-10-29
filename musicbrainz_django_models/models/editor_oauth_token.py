"""
.. module:: editor_oauth_token

The **Editor Oauth Token** Model.

PostgreSQL Definition
---------------------

The :code:`editor_oauth_token` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_oauth_token
    (
        id                  SERIAL,
        editor              INTEGER NOT NULL, -- references editor.id
        application         INTEGER NOT NULL, -- references application.id
        authorization_code  TEXT,
        refresh_token       TEXT,
        access_token        TEXT,
        expire_time         TIMESTAMP WITH TIME ZONE NOT NULL,
        scope               INTEGER NOT NULL DEFAULT 0,
        granted             TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_oauth_token(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: References :class:`editor`.
    :param application: References :class:`application`.
    """

    id = models.AutoField(primary_key=True)
    editor = models.ForeignKey('editor')
    application = models.ForeignKey('application')
    authorization_code = models.TextField(null=True)
    refresh_token = models.TextField(null=True)
    access_token = models.TextField(null=True)
    expire_time = models.DateTimeField()
    scope = models.IntegerField(default=0)
    granted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Editor OAuth Token'

    class Meta:
        db_table = 'editor_oauth_token'
