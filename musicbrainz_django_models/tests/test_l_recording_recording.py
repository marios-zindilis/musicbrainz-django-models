from django.test import TestCase
from ..models import l_recording_recording


class test_l_recording_recording(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_recording_recording()

    def test__l_recording_recording__instance(self):
        self.assertIsInstance(self.subject, l_recording_recording)

    def test__l_recording_recording__str(self):
        self.assertEqual(str(self.subject), 'L Recording Recording')
