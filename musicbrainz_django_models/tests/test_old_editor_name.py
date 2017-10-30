from django.test import TestCase
from ..models import old_editor_name


class test_old_editor_name(TestCase):
    def setUp(self):
        self.subject = old_editor_name(name='Name')

    def test__old_editor_name__instance(self):
        self.assertIsInstance(self.subject, old_editor_name)

    def test__old_editor_name__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
