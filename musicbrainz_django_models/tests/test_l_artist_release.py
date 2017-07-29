from django.test import TestCase
from ..models import l_artist_release


class test_l_artist_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_release()

    def test__l_artist_release__instance(self):
        self.assertIsInstance(self.subject, l_artist_release)

    def test__l_artist_release__str(self):
        self.assertEqual(str(self.subject), 'L Artist Release')
