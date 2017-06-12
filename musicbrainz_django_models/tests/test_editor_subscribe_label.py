from django.test import TestCase
from ..models import editor_subscribe_label


class test_editor_subscribe_label(TestCase):
    def setUp(self):
        self.subject = editor_subscribe_label()

    def test__editor_subscribe_label__instance(self):
        self.assertIsInstance(self.subject, editor_subscribe_label)

    def test__editor_subscribe_label__str(self):
        self.assertEqual(str(self.subject), 'Editor Subscribe Label')
