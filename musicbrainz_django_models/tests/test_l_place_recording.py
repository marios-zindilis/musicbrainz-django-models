from django.test import TestCase
from ..models import l_place_recording


class test_l_place_recording(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_place_recording()

    def test__l_place_recording__instance(self):
        self.assertIsInstance(self.subject, l_place_recording)

    def test__l_place_recording__str(self):
        self.assertEqual(str(self.subject), 'L Place Recording')
