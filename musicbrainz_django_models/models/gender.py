"""
.. module:: gender

The **Gender** Model is referenced by the :code:`artist` and the
:code:`editor` models. Here's a complete table of values, from the MusicBrainz
database dump of 2017-04-19:

+----+--------+--------+-------------+-------------+--------------------------------------+
| id | name   | parent | child_order | description | gid                                  |
+====+========+========+=============+=============+======================================+
|  1 | Male   |        |           1 |             | 36d3d30a-839d-3eda-8cb3-29be4384e4a9 |
+----+--------+--------+-------------+-------------+--------------------------------------+
|  2 | Female |        |           2 |             | 93452b5a-a947-30c8-934f-6a4056b151c2 |
+----+--------+--------+-------------+-------------+--------------------------------------+
|  3 | Other  |        |           3 |             | 081c0bf5-da60-37b0-95f8-2207a3f7f9d6 |
+----+--------+--------+-------------+-------------+--------------------------------------+

PostgreSQL Definition
---------------------

The :code:`gender` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE gender ( -- replicate
        id                  SERIAL,
        name                VARCHAR(255) NOT NULL,
        parent              INTEGER, -- references gender.id
        child_order         INTEGER NOT NULL DEFAULT 0,
        description         TEXT,
        gid                 uuid NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..signals import pre_save_name_is_member_of_name_choices_list
from . import abstract


@python_2_unicode_compatible
class gender(abstract.model_type):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param str name: This field is not restricted to a range of values in the
        SQL definition. From the database dumps it is apparent that there are
        3 possible values: "Male", "Female" and "Other". This is implemented
        in Django with a `choices` parameter to the `name` field, as well as
        with a `pre_save` signal for validation.
    """

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    NAME_CHOICES = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (OTHER, OTHER),
    )
    NAME_CHOICES_LIST = [_[0] for _ in NAME_CHOICES]

    name = models.CharField(max_length=255, choices=NAME_CHOICES)

    class Meta:
        db_table = 'gender'


models.signals.pre_save.connect(pre_save_name_is_member_of_name_choices_list, sender=gender)
