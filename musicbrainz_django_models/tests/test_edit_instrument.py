from django.test import TestCase
from ..models import edit_instrument


class test_edit_instrument(TestCase):
    def setUp(self):
        self.subject = edit_instrument()

    def test__edit_instrument__instance(self):
        self.assertIsInstance(self.subject, edit_instrument)

    def test__edit_instrument__str(self):
        self.assertEqual(str(self.subject), 'Edit Instrument')
