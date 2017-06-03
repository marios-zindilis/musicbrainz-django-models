from django.test import TestCase
from ..models import edit_area


class test_edit_area(TestCase):
    def setUp(self):
        self.subject = edit_area()

    def test__edit_area__instance(self):
        self.assertIsInstance(self.subject, edit_area)

    def test__edit_area__str(self):
        self.assertEqual(str(self.subject), 'Edit Area')
