from django.test import TestCase
from ..models import l_artist_url


class test_l_artist_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_url()

    def test__l_artist_url__instance(self):
        self.assertIsInstance(self.subject, l_artist_url)

    def test__l_artist_url__str(self):
        self.assertEqual(str(self.subject), 'L Artist Url')
