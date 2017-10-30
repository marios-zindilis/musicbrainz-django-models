from django.test import TestCase
from ..models import release_country


class test_release_country(TestCase):
    def setUp(self):
        self.subject = release_country()

    def test__release_country__instance(self):
        self.assertIsInstance(self.subject, release_country)

    def test__release_country__str(self):
        self.assertEqual(str(self.subject), 'Release Country')
