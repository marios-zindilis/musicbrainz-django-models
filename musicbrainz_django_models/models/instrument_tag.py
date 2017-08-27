"""
.. module:: instrument_tag

The **Instrument Tag** Model.

PostgreSQL Definition
---------------------

The :code:`instrument_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE instrument_tag ( -- replicate (verbose)
        instrument          INTEGER NOT NULL, -- PK, references instrument.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class instrument_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param instrument: References :class:`instrument`.
    """

    instrument = models.OneToOneField('instrument', primary_key=True)

    def __str__(self):
        return 'Instrument Tag'

    class Meta:
        db_table = 'instrument_tag'
