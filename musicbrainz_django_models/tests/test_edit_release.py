from django.test import TestCase
from ..models import edit_release


class test_edit_release(TestCase):
    def setUp(self):
        self.subject = edit_release()

    def test__edit_release__instance(self):
        self.assertIsInstance(self.subject, edit_release)

    def test__edit_release__str(self):
        self.assertEqual(str(self.subject), 'Edit Release')
