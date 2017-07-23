from django.test import TestCase
from ..models import iso_3166_3


class test_iso_3166_3(TestCase):
    def setUp(self):
        self.subject = iso_3166_3()

    def test__iso_3166_3__instance(self):
        self.assertIsInstance(self.subject, iso_3166_3)

    def test__iso_3166_3__str(self):
        self.assertEqual(str(self.subject), 'ISO 3166_3')
