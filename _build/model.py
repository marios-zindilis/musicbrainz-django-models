#!/usr/bin/env python3
import sys

try:
    MODEL_NAME = sys.argv[1]
except IndexError:
    print('Model Name Not Provided')
    exit(1)

MODEL_NAME_TITLE = MODEL_NAME.title().replace('_', ' ')
MODEL = 'musicbrainz_django_models/models/{}.py'.format(MODEL_NAME)
INIT = 'musicbrainz_django_models/models/__init__.py'
SQL = '_etc/CreateTables.sql'
SQL_EXISTS = False
SQL_TABLE = []
SQL_TABLE_INCLUDES_ID = False
SQL_TABLE_INCLUDES_GID = False
IMPORTS = [
    'from django.db import models',
    'from django.utils.encoding import python_2_unicode_compatible',
]
FIELDS = []
GID_DOC = ''
MODELS = []
MODEL_TEMPLATE = '''"""
.. module:: {MODEL_NAME}

The **{MODEL_NAME_TITLE}** Model.

PostgreSQL Definition
---------------------

The :code:`{MODEL_NAME}` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    {SQL_TABLE}
"""

{IMPORTS}


@python_2_unicode_compatible
class {MODEL_NAME}(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    {GID_DOC}
    """

{FIELDS}

    def __str__(self):
        return self.name

    class Meta:
        db_table = '{MODEL_NAME}'
'''

with open(SQL, 'r') as sql:
    for line in sql:
        if (
            line.startswith('CREATE TABLE {} '.format(MODEL_NAME)) or
            line == 'CREATE TABLE {}\n'.format(MODEL_NAME)
        ):
            SQL_EXISTS = True
            break

if not SQL_EXISTS:
    print('CREATE TABLE {} Not Found'.format(MODEL_NAME))
    exit(1)

with open(SQL, 'r') as sql:
    SQL_TABLE_CAPTURE = False
    for line in sql:
        if (
            line.startswith('CREATE TABLE {} '.format(MODEL_NAME)) or
            line == 'CREATE TABLE {}\n'.format(MODEL_NAME)
        ):
            SQL_TABLE_CAPTURE = True
        if SQL_TABLE_CAPTURE and line.startswith(');'):
            SQL_TABLE.append(line)
            SQL_TABLE_CAPTURE = False
            break
        if SQL_TABLE_CAPTURE:
            if not SQL_TABLE_INCLUDES_ID:
                SQL_TABLE_INCLUDES_ID = ' serial,' in line.lower()
            if not SQL_TABLE_INCLUDES_GID:
                SQL_TABLE_INCLUDES_GID = ' uuid ' in line.lower()
            SQL_TABLE.append(line)

if SQL_TABLE_INCLUDES_ID:
    FIELDS.append('    id = models.AutoField(primary_key=True)')
if SQL_TABLE_INCLUDES_GID:
    IMPORTS.append('import uuid')
    FIELDS.append('    gid = models.UUIDField(default=uuid.uuid4)')
    GID_DOC = """:param gid: this is interesting because it cannot be NULL but a default is
        not defined in SQL. The default `uuid.uuid4` in Django will generate a
        UUID during the creation of an instance."""

print('MODEL_NAME: {}'.format(MODEL_NAME))
print(''.join(SQL_TABLE))

with open(MODEL, 'w') as model:
    model.write(MODEL_TEMPLATE.format(
        MODEL_NAME=MODEL_NAME,
        MODEL_NAME_TITLE=MODEL_NAME_TITLE,
        SQL_TABLE='    '.join(SQL_TABLE),
        IMPORTS='\n'.join(IMPORTS),
        FIELDS='\n'.join(FIELDS),
        GID_DOC=GID_DOC
    ))

with open(INIT, 'r') as init:
    MODELS = [line.split()[-1] for line in init if line.startswith('from ')]
    MODELS.append(MODEL_NAME)

with open(INIT, 'w') as init:
    for mod in MODELS:
        init.write('from .{mod} import {mod}\n'.format(mod=mod))
    init.write('\n')
    init.write('# __all__ silences PEP8 `module imported but unused`:\n')
    init.write('__all__ = [\n')
    for mod in MODELS:
        init.write('    {mod},\n'.format(mod=mod))
    init.write(']\n')
