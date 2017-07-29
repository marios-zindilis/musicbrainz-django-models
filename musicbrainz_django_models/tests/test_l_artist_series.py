from django.test import TestCase
from ..models import l_artist_series


class test_l_artist_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_series()

    def test__l_artist_series__instance(self):
        self.assertIsInstance(self.subject, l_artist_series)

    def test__l_artist_series__str(self):
        self.assertEqual(str(self.subject), 'L Artist Series')
