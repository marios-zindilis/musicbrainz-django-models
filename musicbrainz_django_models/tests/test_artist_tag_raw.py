from django.test import TestCase
from ..models import artist_tag_raw


class test_artist_tag_raw(TestCase):
    def setUp(self):
        self.subject = artist_tag_raw()

    def test__artist_tag_raw__instance(self):
        self.assertIsInstance(self.subject, artist_tag_raw)

    def test__artist_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Artist Tag Raw')
