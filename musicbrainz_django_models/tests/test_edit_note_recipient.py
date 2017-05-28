from django.test import TestCase
from ..models import edit_note_recipient


class test_edit_note_recipient(TestCase):
    def setUp(self):
        self.subject = edit_note_recipient()

    def test__edit_note_recipient__instance(self):
        self.assertIsInstance(self.subject, edit_note_recipient)

    def test__edit_note_recipient__str(self):
        self.assertEqual(str(self.subject), 'Edit Note Recipient')
