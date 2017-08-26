"""
.. module:: label_meta

The **Label Meta** Model.

PostgreSQL Definition
---------------------

The :code:`label_meta` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_meta ( -- replicate
        id                  INTEGER NOT NULL, -- PK, references label.id CASCADE
        rating              SMALLINT CHECK (rating >= 0 AND rating <= 100),
        rating_count        INTEGER
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_meta import abstract__model_meta


@python_2_unicode_compatible
class label_meta(abstract__model_meta):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param int id: references :class:`.label`. This is both a foreign and a
        primary key, best implemented in Django as a `OneToOneField`.
    """

    id = models.OneToOneField('label', primary_key=True)

    def __str__(self):
        return 'Label Meta'

    class Meta:
        db_table = 'label_meta'
