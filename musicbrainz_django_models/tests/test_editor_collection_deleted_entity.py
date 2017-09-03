from django.test import TestCase
from ..models import editor_collection_deleted_entity


class test_editor_collection_deleted_entity(TestCase):
    def setUp(self):
        self.subject = editor_collection_deleted_entity()

    def test__editor_collection_deleted_entity__instance(self):
        self.assertIsInstance(self.subject, editor_collection_deleted_entity)

    def test__editor_collection_deleted_entity__str(self):
        self.assertEqual(str(self.subject), 'Editor Collection Deleted Entity')
