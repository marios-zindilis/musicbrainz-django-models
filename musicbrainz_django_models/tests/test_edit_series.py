from django.test import TestCase
from ..models import edit_series


class test_edit_series(TestCase):
    def setUp(self):
        self.subject = edit_series()

    def test__edit_series__instance(self):
        self.assertIsInstance(self.subject, edit_series)

    def test__edit_series__str(self):
        self.assertEqual(str(self.subject), 'Edit Series')
