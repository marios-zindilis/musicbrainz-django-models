from django.test import TestCase
from ..models import editor


class test_editor(TestCase):
    def setUp(self):
        self.subject = editor(name='Name')

    def test__editor__instance(self):
        self.assertIsInstance(self.subject, editor)

    def test__editor__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
