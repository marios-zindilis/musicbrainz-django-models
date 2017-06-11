from django.test import TestCase
from ..models import edit_url


class test_edit_url(TestCase):
    def setUp(self):
        self.subject = edit_url()

    def test__edit_url__instance(self):
        self.assertIsInstance(self.subject, edit_url)

    def test__edit_url__str(self):
        self.assertEqual(str(self.subject), 'Edit URL')
