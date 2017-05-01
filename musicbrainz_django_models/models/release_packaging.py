"""
.. module:: release_packaging

The **Release Packaging** is one of:

1. Jewel Case
2. Slim Jewel Case
3. Digipak
4. Cardboard/Paper Sleeve
5. Other
6. Keep Case
7. None
8. Cassette Case
9. Book
10. Fatbox
11. Snap Case
12. Gatefold Cover
13. Discbox Slider
14. Super Jewel Box
15. Digibook

The Release Packaging is referenced by the Release model. Read more at the
`Release Packaging documentation on MusicBrainz`_.

.. _Release Packaging documentation on MusicBrainz: https://musicbrainz.org/doc/Release/Packaging

PostreSQL Definition
--------------------

The :code:`release_status` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE release_packaging ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references release_packaging.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
import uuid


def pre_save_release_packaging(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'Release Packaging Name "{}" is not one of: {}'.format(
                instance.name,
                ', '.join(sender.NAME_CHOICE_LIST)))


class release_packaging(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of a range of values. This is not
        restricted in the SQL, but it is documented in
        `the Release documentation <https://musicbrainz.org/doc/Release>`_.
        In Django, this is implemented as a `choices` parameter to the `name`
        field, and a `pre_save` signal that performs the validation.
    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    JEWEL_CASE = 'Jewel Case'
    SLIM_JEWEL_CASE = 'Slim Jewel Case'
    DIGIPAK = 'Digipak'
    CARDBOARD_PAPER_SLEEVE = 'Cardboard/Paper Sleeve'
    OTHER = 'Other'
    KEEP_CASE = 'Keep Case'
    NONE = 'None'
    CASSETTE_CASE = 'Cassette Case'
    BOOK = 'Book'
    FATBOX = 'Fatbox'
    SNAP_CASE = 'Snap Case'
    GATEFOLD_COVER = 'Gatefold Cover'
    DISCBOX_SLIDER = 'Discbox Slider'
    SUPER_JEWEL_BOX = 'Super Jewel Box'
    DIGIBOOK = 'Digibook'
    NAME_CHOICES = (
        (JEWEL_CASE, JEWEL_CASE),
        (SLIM_JEWEL_CASE, SLIM_JEWEL_CASE),
        (DIGIPAK, DIGIPAK),
        (CARDBOARD_PAPER_SLEEVE, CARDBOARD_PAPER_SLEEVE),
        (OTHER, OTHER),
        (KEEP_CASE, KEEP_CASE),
        (NONE, NONE),
        (CASSETTE_CASE, CASSETTE_CASE),
        (BOOK, BOOK),
        (FATBOX, FATBOX),
        (SNAP_CASE, SNAP_CASE),
        (GATEFOLD_COVER, GATEFOLD_COVER),
        (DISCBOX_SLIDER, DISCBOX_SLIDER),
        (SUPER_JEWEL_BOX, SUPER_JEWEL_BOX),
        (DIGIBOOK, DIGIBOOK),)
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
        db_table = 'release_packaging'


models.signals.pre_save.connect(
    pre_save_release_packaging, sender=release_packaging)
