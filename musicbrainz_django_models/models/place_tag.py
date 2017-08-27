"""
.. module:: place_tag

The **Place Tag** Model.

PostgreSQL Definition
---------------------

The :code:`place_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE place_tag ( -- replicate (verbose)
        place               INTEGER NOT NULL, -- PK, references place.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class place_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param place: References :class:`place`.
    """

    place = models.OneToOneField('place', primary_key=True)

    def __str__(self):
        return 'Place Tag'

    class Meta:
        db_table = 'place_tag'
