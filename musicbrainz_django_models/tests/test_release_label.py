from django.test import TestCase
from ..models import release_label


class test_release_label(TestCase):
    def setUp(self):
        self.subject = release_label()

    def test__release_label__instance(self):
        self.assertIsInstance(self.subject, release_label)

    def test__release_label__str(self):
        self.assertEqual(str(self.subject), 'Release Label')
