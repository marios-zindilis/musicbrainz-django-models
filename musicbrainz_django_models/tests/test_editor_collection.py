from django.test import TestCase
from ..models import editor_collection


class test_editor_collection(TestCase):
    def setUp(self):
        self.subject = editor_collection(name='Name')

    def test__editor_collection__instance(self):
        self.assertIsInstance(self.subject, editor_collection)

    def test__editor_collection__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
