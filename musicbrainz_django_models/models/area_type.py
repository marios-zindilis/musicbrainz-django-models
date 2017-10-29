"""
.. module:: area_type

The **Area Type** is either a Country, a Subdivision, a County, a
Municipality, a City, a District or an Island. It is referenced by the
:code:`area` Model.

PostreSQL Definition
--------------------

The :code:`area_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE area_type ( -- replicate
        id                  SERIAL, -- PK
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references area_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_name_is_member_of_name_choices_list
from .abstract__model_type import abstract__model_type


@python_2_unicode_compatible
class area_type(abstract__model_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of the following values: "Country",
        "Subdivision", "County", "Municipality", "City", "District" and
        "Island". This is not restricted in the SQL, but it is documented in
        `the Area documentation <https://musicbrainz.org/doc/Area>`_. In
        Django, this is implemented as a `choices` parameter to the `name`
        field, and a `pre_save` signal that performs the validation.
    """

    COUNTRY = 'Country'
    SUBDIVISION = 'Subdivision'
    COUNTY = 'County'
    MUNICIPALITY = 'Municipality'
    CITY = 'City'
    DISTRICT = 'District'
    ISLAND = 'Island'
    NAME_CHOICES = (
        (COUNTRY, COUNTRY),
        (SUBDIVISION, SUBDIVISION),
        (COUNTY, COUNTY),
        (MUNICIPALITY, MUNICIPALITY),
        (CITY, CITY),
        (DISTRICT, DISTRICT),
        (ISLAND, ISLAND),)
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.CharField(max_length=255, choices=NAME_CHOICES)

    class Meta:
        db_table = 'area_type'
        verbose_name_plural = 'Area Types'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=area_type)
