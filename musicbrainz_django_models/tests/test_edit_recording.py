from django.test import TestCase
from ..models import edit_recording


class test_edit_recording(TestCase):
    def setUp(self):
        self.subject = edit_recording()

    def test__edit_recording__instance(self):
        self.assertIsInstance(self.subject, edit_recording)

    def test__edit_recording__str(self):
        self.assertEqual(str(self.subject), 'Edit Recording')
