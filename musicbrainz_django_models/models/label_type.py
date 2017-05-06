"""
.. module:: label_type

The **Label Type** model. The value can be one of:

1. Distributor
2. Holding
3. Production
4. Original Production
5. Bootleg Production
6. Reissue Production
7. Publisher
8. Rights
9. Imprint

Here's a complete table, from the MusicBrainz Server database dump of 2017-04-19:

+----+---------------------+--------+-------------+-------------+--------------------------------------+
| id | name                | parent | child_order | description | uuid                                 |
+====+=====================+========+=============+=============+======================================+
|  1 | Distributor         |        |           0 |             | 53ab8dcc-9946-3b62-966e-7634d78e5034 |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  2 | Holding             |        |           0 |             | 43f31a62-97e4-36f6-9752-453c131b71ed |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  3 | Production          |        |           0 |             | a2426aab-2dd4-339c-b47d-b4923a241678 |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  4 | Original Production |      3 |           0 |             | 7aaa37fe-2def-3476-b359-80245850062d |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  5 | Bootleg Production  |      3 |           0 |             | fdac9b96-359b-3488-9322-ad99c2473636 |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  6 | Reissue Production  |      3 |           0 |             | 88ee6ae7-f413-3490-a1d2-54f6a9f0838c |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  7 | Publisher           |        |           0 |             | e9ad53b0-e3d0-3885-a10b-8193d501338c |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  8 | Rights Society      |        |           0 |             | 78ab2758-7809-372c-9b99-74b7ab87f390 |
+----+---------------------+--------+-------------+-------------+--------------------------------------+
|  9 | Imprint             |        |           0 |             | b6285b2a-3514-3d43-80df-fcf528824ded |
+----+---------------------+--------+-------------+-------------+--------------------------------------+


PostreSQL Definition
--------------------

The :code:`label_type` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE label_type ( -- replicate
        id                  SERIAL, -- PK
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references label_type.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


def pre_save_label_type(sender, instance, **kwargs):
    if instance.name not in sender.NAME_CHOICE_LIST:
        from django.core.exceptions import ValidationError
        raise ValidationError('Label Type Name "{}" is not one of: {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICE_LIST)))


@python_2_unicode_compatible
class label_type(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: the name can be one of a range of values. This is not
        restricted in the SQL, but it is documented in
        `the Label Type documentation <https://musicbrainz.org/doc/Label/Type>`_.
        In Django, this is implemented as a `choices` parameter to the `name`
        field, and a `pre_save` signal that performs the validation.
    :param gid: This cannot be NULL but a default is not defined in SQL. The
        `default=uuid.uuid4` in Django will generate a UUID during the creation
        of an instance.
    """

    DISTRIBUTOR = 'Distributor'
    HOLDING = 'Holding'
    PRODUCTION = 'Production'
    ORIGINAL_PRODUCTION = 'Original Production'
    BOOTLEG_PRODUCTION = 'Bootleg Production'
    REISSUE_PRODUCTION = 'Reissue Production'
    PUBLISHER = 'Publisher'
    RIGHTS_SOCIETY = 'Rights Society'
    IMPRINT = 'Imprint'
    NAME_CHOICES = (
        (DISTRIBUTOR, DISTRIBUTOR),
        (HOLDING, HOLDING),
        (PRODUCTION, PRODUCTION),
        (ORIGINAL_PRODUCTION, ORIGINAL_PRODUCTION),
        (BOOTLEG_PRODUCTION, BOOTLEG_PRODUCTION),
        (REISSUE_PRODUCTION, REISSUE_PRODUCTION),
        (PUBLISHER, PUBLISHER),
        (RIGHTS_SOCIETY, RIGHTS_SOCIETY),
        (IMPRINT, IMPRINT),)
    NAME_CHOICE_LIST = [_[0] for _ in NAME_CHOICES]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    parent = models.ForeignKey('self', null=True)
    child_order = models.IntegerField(default=0)
    description = models.TextField(null=True)
    gid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'label_type'
        verbose_name_plural = 'Label Types'


models.signals.pre_save.connect(pre_save_label_type, sender=label_type)
