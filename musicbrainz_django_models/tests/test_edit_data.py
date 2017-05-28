from django.test import TestCase
from ..models import edit_data


class test_edit_data(TestCase):
    def setUp(self):
        self.subject = edit_data()

    def test__edit_data__instance(self):
        self.assertIsInstance(self.subject, edit_data)

    def test__edit_data__str(self):
        self.assertEqual(str(self.subject), 'Edit Data')
