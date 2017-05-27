"""
.. module:: area_annotation

The **Area Annotation** Model.

PostgreSQL Definition
---------------------

The :code:`area_annotation` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_annotation ( -- replicate (verbose)
        area        INTEGER NOT NULL, -- PK, references area.id
        annotation  INTEGER NOT NULL -- PK, references annotation.id
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class area_annotation(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param area: references :class:`.area`. This field is interesting because
        it is both a Foreign Key to the Area model, as well as the Primary Key
        for the Area Annotation model. In Django, this can be implemented as a
        `OneToOneField`.
    :param annotation: references :class:`.annotation`. Both the `area` and
        the the `annotation` fields are primary keys in the SQL. In Django,
        there can only be 1 primary key per model. The uniqueness required for
        a primary key can be implemented in Django with a `OneToOneField`.
    """

    area = models.OneToOneField('area', primary_key=True)
    annotation = models.OneToOneField('annotation')

    def __str__(self):
        return 'Area Annotation'

    class Meta:
        db_table = 'area_annotation'
        verbose_name_plural = 'Area Annotation'
