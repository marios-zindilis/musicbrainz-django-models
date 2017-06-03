from django.test import TestCase
from ..models import edit_place


class test_edit_place(TestCase):
    def setUp(self):
        self.subject = edit_place()

    def test__edit_place__instance(self):
        self.assertIsInstance(self.subject, edit_place)

    def test__edit_place__str(self):
        self.assertEqual(str(self.subject), 'Edit Place')
