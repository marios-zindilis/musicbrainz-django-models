from django.test import TestCase
from ..models import l_recording_release


class test_l_recording_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_recording_release()

    def test__l_recording_release__instance(self):
        self.assertIsInstance(self.subject, l_recording_release)

    def test__l_recording_release__str(self):
        self.assertEqual(str(self.subject), 'L Recording Release')
