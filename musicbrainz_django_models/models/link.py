"""
.. module:: link

The **Link** Model.

PostgreSQL Definition
---------------------

The :code:`link` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE link ( -- replicate
        id                  SERIAL,
        link_type           INTEGER NOT NULL, -- references link_type.id
        begin_date_year     SMALLINT,
        begin_date_month    SMALLINT,
        begin_date_day      SMALLINT,
        end_date_year       SMALLINT,
        end_date_month      SMALLINT,
        end_date_day        SMALLINT,
        attribute_count     INTEGER NOT NULL DEFAULT 0,
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        ended               BOOLEAN NOT NULL DEFAULT FALSE
          CONSTRAINT link_ended_check CHECK (
            (
              -- If any end date fields are not null, then ended must be true
              (end_date_year IS NOT NULL OR
               end_date_month IS NOT NULL OR
               end_date_day IS NOT NULL) AND
              ended = TRUE
            ) OR (
              -- Otherwise, all end date fields must be null
              (end_date_year IS NULL AND
               end_date_month IS NULL AND
               end_date_day IS NULL)
            )
          )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


def pre_save_link(sender, instance, **kwargs):
    instance.ended = (
        instance.end_date_year is not None or
        instance.end_date_month is not None or
        instance.end_date_day is not None)


@python_2_unicode_compatible
class link(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param smallint begin_date_month: You'd think this would be validated as a
        range of 1-12 or similar...
    :param smallint end_date_month: ditto
    :param smallint begin_date_day: You'd think this would be validated as a
        range of 1-31 or similar...
    :param smallint end_date_day: ditto
    :param boolean ended: the MusicBrainz Server uses a PostgreSQL `check` to
        set this to `True` if any of the `end_*` fields has any value. This is
        implemented in Django with a `pre_save` signal.
    """

    id = models.AutoField(primary_key=True)
    link_type = models.ForeignKey('link_type')
    begin_date_year = models.SmallIntegerField(null=True)
    begin_date_month = models.SmallIntegerField(null=True)
    begin_date_day = models.SmallIntegerField(null=True)
    end_date_year = models.SmallIntegerField(null=True)
    end_date_month = models.SmallIntegerField(null=True)
    end_date_day = models.SmallIntegerField(null=True)
    attribute_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return 'Link'

    class Meta:
        db_table = 'link'


models.signals.pre_save.connect(pre_save_link, sender=link)
