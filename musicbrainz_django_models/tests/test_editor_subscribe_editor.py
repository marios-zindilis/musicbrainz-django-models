from django.test import TestCase
from ..models import editor_subscribe_editor


class test_editor_subscribe_editor(TestCase):
    def setUp(self):
        self.subject = editor_subscribe_editor()

    def test__editor_subscribe_editor__instance(self):
        self.assertIsInstance(self.subject, editor_subscribe_editor)

    def test__editor_subscribe_editor__str(self):
        self.assertEqual(str(self.subject), 'Editor Subscribe Editor')
