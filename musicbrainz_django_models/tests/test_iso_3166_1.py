from django.test import TestCase
from ..models import iso_3166_1


class test_iso_3166_1(TestCase):
    def setUp(self):
        self.subject = iso_3166_1()

    def test__iso_3166_1__instance(self):
        self.assertIsInstance(self.subject, iso_3166_1)

    def test__iso_3166_1__str(self):
        self.assertEqual(str(self.subject), 'ISO 3166_1')
