from django.test import TestCase
from ..models import l_recording_series


class test_l_recording_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_recording_series()

    def test__l_recording_series__instance(self):
        self.assertIsInstance(self.subject, l_recording_series)

    def test__l_recording_series__str(self):
        self.assertEqual(str(self.subject), 'L Recording Series')
