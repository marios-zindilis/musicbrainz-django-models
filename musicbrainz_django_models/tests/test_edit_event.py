from django.test import TestCase
from ..models import edit_event


class test_edit_event(TestCase):
    def setUp(self):
        self.subject = edit_event()

    def test__edit_event__instance(self):
        self.assertIsInstance(self.subject, edit_event)

    def test__edit_event__str(self):
        self.assertEqual(str(self.subject), 'Edit Event')
