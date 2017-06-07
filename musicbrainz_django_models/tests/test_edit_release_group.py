from django.test import TestCase
from ..models import edit_release_group


class test_edit_release_group(TestCase):
    def setUp(self):
        self.subject = edit_release_group()

    def test__edit_release_group__instance(self):
        self.assertIsInstance(self.subject, edit_release_group)

    def test__edit_release_group__str(self):
        self.assertEqual(str(self.subject), 'Edit Release Group')
