"""
.. module:: label_alias

The **Label Alias** Model.

PostgreSQL Definition
---------------------

The :code:`label_alias` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_alias ( -- replicate (verbose)
        id                  SERIAL,
        label               INTEGER NOT NULL, -- references label.id
        name                VARCHAR NOT NULL,
        locale              TEXT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        type                INTEGER, -- references label_alias_type.id
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
class label_alias(abstract__model_alias):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param label: References :class:`label`.
    """

    label = models.ForeignKey('label')
    type = models.ForeignKey('label_alias_type', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'label_alias'


models.signals.pre_save.connect(pre_save_model_alias, sender=label_alias)
