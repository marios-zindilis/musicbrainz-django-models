from django.test import TestCase
from ..models import l_recording_url


class test_l_recording_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_recording_url()

    def test__l_recording_url__instance(self):
        self.assertIsInstance(self.subject, l_recording_url)

    def test__l_recording_url__str(self):
        self.assertEqual(str(self.subject), 'L Recording Url')
