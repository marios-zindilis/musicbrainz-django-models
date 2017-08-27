"""
.. module:: label_tag

The **Label Tag** Model.

PostgreSQL Definition
---------------------

The :code:`label_tag` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_tag ( -- replicate (verbose)
        label               INTEGER NOT NULL, -- PK, references label.id
        tag                 INTEGER NOT NULL, -- PK, references tag.id
        count               INTEGER NOT NULL,
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .abstract__model_tag import abstract__model_tag


@python_2_unicode_compatible
class label_tag(abstract__model_tag):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param label: References :class:`label`.
    """

    label = models.OneToOneField('label', primary_key=True)

    def __str__(self):
        return 'Label Tag'

    class Meta:
        db_table = 'label_tag'
