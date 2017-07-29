#!/usr/bin/env python3

SQL = '_etc/CreateTables.sql'
LINK_MODELS = []
INIT = 'musicbrainz_django_models/models/__init__.py'

MODEL_TEMPLATE = '''"""
.. module:: {MODEL_NAME}

The **{MODEL_NAME_TITLE}** Model.

PostgreSQL Definition
---------------------

The :code:`{MODEL_NAME}` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    {SQL_TABLE}
"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class {MODEL_NAME}(models.Model):
    """
    Not all parameters are listed here, only those that present some interest
    in their Django implementation.

    :param int edits_pending: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    :param int link_order: the MusicBrainz Server uses a PostgreSQL `check`
        to validate that the value is a positive integer. In Django, this is
        done with `models.PositiveIntegerField()`.
    """

    id = models.AutoField(primary_key=True)
    link = models.ForeignKey('link')
    entity0 = models.ForeignKey('{ENTITY0}', related_name='links_to_{ENTITY1}')
    entity1 = models.ForeignKey('{ENTITY1}')
    edits_pending = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    link_order = models.PositiveIntegerField(default=0)
    entity0 = models.TextField(default='')
    entity1 = models.TextField(default='')

    def __str__(self):
        return '{MODEL_NAME_TITLE}'

    class Meta:
        db_table = '{MODEL_NAME}'
'''

TEST_TEMPLATE = '''from django.test import TestCase
from ..models import {MODEL_NAME}


class test_{MODEL_NAME}(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = {MODEL_NAME}()

    def test__{MODEL_NAME}__instance(self):
        self.assertIsInstance(self.subject, {MODEL_NAME})

    def test__{MODEL_NAME}__str(self):
        self.assertEqual(str(self.subject), '{MODEL_NAME_TITLE}')
'''

# Build the link models list:
with open(SQL, 'r') as sql:
    for line in sql:
        if line.startswith('CREATE TABLE l_'):
            LINK_MODELS.append(line.split()[2])

with open(INIT, 'r') as init:
    MODELS_IN_INIT = [line.split()[-1] for line in init if line.startswith('from ')]

for model in LINK_MODELS:
    MODEL = 'musicbrainz_django_models/models/{}.py'.format(model)
    TEST = 'musicbrainz_django_models/tests/test_{}.py'.format(model)
    SQL_TABLE = []
    with open(SQL, 'r') as sql:
        SQL_TABLE_CAPTURE = False
        for line in sql:
            if line.startswith('CREATE TABLE {} ( -- replicate'.format(model)):
                SQL_TABLE_CAPTURE = True
            if SQL_TABLE_CAPTURE and line.startswith(');'):
                SQL_TABLE.append(line)
                SQL_TABLE_CAPTURE = False
                break
            if SQL_TABLE_CAPTURE:
                if line.split()[0] == 'entity0':
                    ENTITY0 = line.split()[-1].split('.')[0]
                if line.split()[0] == 'entity1':
                    ENTITY1 = line.split()[-1].split('.')[0]
                SQL_TABLE.append(line)

    TEMPLATE_VARS = {
        'MODEL_NAME': model,
        'MODEL_NAME_TITLE': model.title().replace('_', ' '),
        'ENTITY0': ENTITY0,
        'ENTITY1': ENTITY1,
        'SQL_TABLE': '    '.join(SQL_TABLE),
    }

    # print(MODEL_TEMPLATE.format(**TEMPLATE_VARS))
    with open(MODEL, 'w') as model_file:
        model_file.write(MODEL_TEMPLATE.format(**TEMPLATE_VARS))
    with open(TEST, 'w') as model_test:
        model_test.write(TEST_TEMPLATE.format(**TEMPLATE_VARS))

    MODELS_IN_INIT.append(model)

with open(INIT, 'w') as init:
    for mod in MODELS_IN_INIT:
        init.write('from .{mod} import {mod}\n'.format(mod=mod))
    init.write('\n')
    init.write('# __all__ silences PEP8 `module imported but unused`:\n')
    init.write('__all__ = [\n')
    for mod in MODELS_IN_INIT:
        init.write('    {mod},\n'.format(mod=mod))
    init.write(']\n')
