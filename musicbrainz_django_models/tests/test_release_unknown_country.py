from django.test import TestCase
from ..models import release_unknown_country


class test_release_unknown_country(TestCase):
    def setUp(self):
        self.subject = release_unknown_country()

    def test__release_unknown_country__instance(self):
        self.assertIsInstance(self.subject, release_unknown_country)

    def test__release_unknown_country__str(self):
        self.assertEqual(str(self.subject), 'Release Unknown Country')
