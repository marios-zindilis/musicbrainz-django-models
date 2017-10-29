"""
.. module:: editor_watch_preferences

The **Editor Watch Preferences** Model.

PostgreSQL Definition
---------------------

The :code:`editor_watch_preferences` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE editor_watch_preferences
    (
        editor INTEGER NOT NULL, -- PK, references editor.id CASCADE
        notify_via_email BOOLEAN NOT NULL DEFAULT TRUE,
        notification_timeframe INTERVAL NOT NULL DEFAULT '1 week',
        last_checked TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class editor_watch_preferences(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param editor: references :class:`editor`. This is both a foreign key to
        the Editor model, as well as the primary key of this model. This is
        nicely implemented in Django with a OneToOneField.
    :param notification_timeframe: This is a PostgreSQL-specific data type.
        For compatibility with other database engines, it is implemented here
        as a CharField.
    """

    editor = models.OneToOneField('editor', primary_key=True)
    notify_via_email = models.BooleanField(default=True)
    notification_timeframe = models.CharField(max_length=256, default='1 week')
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Editor Watch Preferences'

    class Meta:
        db_table = 'editor_watch_preferences'
