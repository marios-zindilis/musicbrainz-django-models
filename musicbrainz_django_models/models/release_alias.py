"""
.. module:: release_alias

The **Release Alias** Model.

PostgreSQL Definition
---------------------

The :code:`release_alias` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_alias ( -- replicate (verbose)
        id                  SERIAL, --PK
        release             INTEGER NOT NULL, -- references release.id
        name                VARCHAR NOT NULL,
        locale              TEXT,
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >=0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        type                INTEGER, -- references release_alias_type.id
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
                 CONSTRAINT primary_check
                     CHECK ((locale IS NULL AND primary_for_locale IS FALSE) OR (locale IS NOT NULL)));

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_alias import abstract__model_alias


@python_2_unicode_compatible
class release_alias(abstract__model_alias):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param release: References :class:`release`.
    :param type: References :class:`release_alias_type`.
    """

    release = models.ForeignKey('release')
    type = models.ForeignKey('release_alias_type')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'release_alias'
