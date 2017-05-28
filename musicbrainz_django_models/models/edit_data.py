"""
.. module:: edit_data

The **Edit Data** Model.

PostgreSQL Definition
---------------------

The :code:`edit_data` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE edit_data
    (
        edit                INTEGER NOT NULL, -- PK, references edit.id
        data                JSONB NOT NULL
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class edit_data(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param data: This field uses the Postgres-specific data type `jsonb`, see:

        https://www.postgresql.org/docs/9.6/static/datatype-json.html

        This has a lot of value-added functionality in Postgres, like indexing
        and queries of the key-value pairs in the stored JSON. In Django,
        there is no backend-independent model field that can offer those
        features, because the implementation is Postgres-specific. The closest
        is a `TextField`, with JSON-specific functionality added as model
        methods.
    """

    edit = models.ForeignKey('edit')
    data = models.TextField()

    def __str__(self):
        return 'Edit Data'

    class Meta:
        db_table = 'edit_data'
