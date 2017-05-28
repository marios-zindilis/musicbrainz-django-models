from django.test import TestCase
from ..models import edit_note


class test_edit_note(TestCase):
    def setUp(self):
        self.subject = edit_note()

    def test__edit_note__instance(self):
        self.assertIsInstance(self.subject, edit_note)

    def test__edit_note__str(self):
        self.assertEqual(str(self.subject), 'Edit Note')
