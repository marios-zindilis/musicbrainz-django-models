"""
.. module:: deleted_entity

The **Deleted Entity** Model.

PostgreSQL Definition
---------------------

The :code:`deleted_entity` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE deleted_entity (
        gid UUID NOT NULL, -- PK
        data JSONB NOT NULL,
        deleted_at timestamptz NOT NULL DEFAULT now()
    );

"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class deleted_entity(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param gid: This is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance.
    :param data: This field uses the Postgres-specific data type `jsonb`, see:

        https://www.postgresql.org/docs/9.6/static/datatype-json.html

        This has a lot of value-added functionality in Postgres, like indexing
        and queries of the key-value pairs in the stored JSON. In Django,
        there is no backend-independent model field that can offer those
        features, because the implementation is Postgres-specific. The closest
        is a `TextField`, with JSON-specific functionality added as model
        methods.
    """

    gid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    data = models.TextField()
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Deleted Entity'

    class Meta:
        db_table = 'deleted_entity'
