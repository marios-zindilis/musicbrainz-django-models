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
import uuid


def validate_area_type_name_choice(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError('Area Type Name "{}" is not one of: {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICE_LIST)))


class area_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of the following values: "Country",
        "Subdivision", "County", "Municipality", "City", "District" and
        "Island". This is not restricted in the SQL, but it is documented in
        `the Area documentation <https://musicbrainz.org/doc/Area>`_. In
        Django, this is implemented as a `choices` parameter to the `name`
        field, and a `pre_save` signal that performs the validation.
    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
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
    NAME_CHOICE_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'area_type'
        verbose_name_plural = 'Area Types'


models.signals.pre_save.connect(
    validate_area_type_name_choice, sender=area_type)
