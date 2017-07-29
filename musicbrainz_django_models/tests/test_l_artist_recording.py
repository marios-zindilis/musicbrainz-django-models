from django.test import TestCase
from ..models import l_artist_recording


class test_l_artist_recording(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_recording()

    def test__l_artist_recording__instance(self):
        self.assertIsInstance(self.subject, l_artist_recording)

    def test__l_artist_recording__str(self):
        self.assertEqual(str(self.subject), 'L Artist Recording')
