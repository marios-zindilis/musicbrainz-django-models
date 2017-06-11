from django.test import TestCase
from ..models import editor_preference


class test_editor_preference(TestCase):
    def setUp(self):
        self.subject = editor_preference()

    def test__editor_preference__instance(self):
        self.assertIsInstance(self.subject, editor_preference)

    def test__editor_preference__str(self):
        self.assertEqual(str(self.subject), 'Editor Preference')
