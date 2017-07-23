from django.test import TestCase
from ..models import iso_3166_2


class test_iso_3166_2(TestCase):
    def setUp(self):
        self.subject = iso_3166_2()

    def test__iso_3166_2__instance(self):
        self.assertIsInstance(self.subject, iso_3166_2)

    def test__iso_3166_2__str(self):
        self.assertEqual(str(self.subject), 'ISO 3166_2')
