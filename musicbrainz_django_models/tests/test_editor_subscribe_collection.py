from django.test import TestCase
from ..models import editor_subscribe_collection


class test_editor_subscribe_collection(TestCase):
    def setUp(self):
        self.subject = editor_subscribe_collection()

    def test__editor_subscribe_collection__instance(self):
        self.assertIsInstance(self.subject, editor_subscribe_collection)

    def test__editor_subscribe_collection__str(self):
        self.assertEqual(str(self.subject), 'Editor Subscribe Collection')
