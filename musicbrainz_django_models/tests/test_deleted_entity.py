from django.test import TestCase
from ..models import deleted_entity


class test_deleted_entity(TestCase):
    def setUp(self):
        self.subject = deleted_entity()

    def test__deleted_entity__instance(self):
        self.assertIsInstance(self.subject, deleted_entity)

    def test__deleted_entity__str(self):
        self.assertEqual(str(self.subject), 'Deleted Entity')
