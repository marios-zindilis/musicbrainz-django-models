from django.test import TestCase
from ..models import artist_tag


class test_artist_tag(TestCase):
    def setUp(self):
        self.subject = artist_tag()

    def test__artist_tag__instance(self):
        self.assertIsInstance(self.subject, artist_tag)

    def test__artist_tag__str(self):
        self.assertEqual(str(self.subject), 'Artist Tag')
