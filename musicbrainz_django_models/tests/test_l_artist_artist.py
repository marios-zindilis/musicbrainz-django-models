from django.test import TestCase
from ..models import l_artist_artist


class test_l_artist_artist(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_artist()

    def test__l_artist_artist__instance(self):
        self.assertIsInstance(self.subject, l_artist_artist)

    def test__l_artist_artist__str(self):
        self.assertEqual(str(self.subject), 'L Artist Artist')
