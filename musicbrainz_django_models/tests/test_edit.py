from django.test import TestCase
from ..models import edit


class test_edit(TestCase):
    def setUp(self):
        self.subject = edit()

    def test__edit__instance(self):
        self.assertIsInstance(self.subject, edit)

    def test__edit__str(self):
        self.assertEqual(str(self.subject), 'Edit')
