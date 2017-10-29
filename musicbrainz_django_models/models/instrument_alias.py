"""
.. module:: instrument_alias

The **Instrument Alias** Model.

PostgreSQL Definition
---------------------

The :code:`instrument_alias` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_alias ( -- replicate (verbose)
        id                  SERIAL, --PK
        instrument          INTEGER NOT NULL, -- references instrument.id
        name                VARCHAR NOT NULL,
        locale              TEXT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >=0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        type                INTEGER, -- references instrument_alias_type.id
        sort_name           VARCHAR NOT NULL,
        begin_date_year     SMALLINT,
        begin_date_month    SMALLINT,
        begin_date_day      SMALLINT,
        end_date_year       SMALLINT,
        end_date_month      SMALLINT,
        end_date_day        SMALLINT,
        primary_for_locale  BOOLEAN NOT NULL DEFAULT false,
        ended               BOOLEAN NOT NULL DEFAULT FALSE
          CHECK (
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
          ),
        CONSTRAINT primary_check CHECK ((locale IS NULL AND primary_for_locale IS FALSE) OR (locale IS NOT NULL)),
        CONSTRAINT search_hints_are_empty
          CHECK (
            (type <> 2) OR (
              type = 2 AND sort_name = name AND
              begin_date_year IS NULL AND begin_date_month IS NULL AND begin_date_day IS NULL AND
              end_date_year IS NULL AND end_date_month IS NULL AND end_date_day IS NULL AND
              primary_for_locale IS FALSE AND locale IS NULL
            )
          )
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_alias import abstract__model_alias
from ..signals import pre_save_model_alias


@python_2_unicode_compatible
class instrument_alias(abstract__model_alias):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param instrument: References :class:`instrument`.
    :param type: In the PostgreSQL definition of the `instrument_alias` table,
        there is a `check` on the `type`, that uses a hardcoded value of `2`.
        The `type` with `id=2` in the `instrument_alias_type` table is the
        `Search hint`. If the `type` of the `instrument_alias` is `Search hint`,
        then a number of fields are restricted. `sort_name` must be equal to
        `name`. `begin_date_year`, `begin_date_month`, `begin_date_day`,
        `end_date_year`, `end_date_month`, `end_date_day` and `locale` must all
        be empty. `primary_for_locale` must be False. In Django, this is
        implemented in a `pre_save` signal.
    """

    instrument = models.ForeignKey('instrument')
    type = models.ForeignKey('instrument_alias_type', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'instrument_alias'
        verbose_name_plural = 'Instrument Aliases'


models.signals.pre_save.connect(pre_save_model_alias, sender=instrument_alias)
