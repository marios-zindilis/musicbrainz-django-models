from django.test import TestCase
from ..models import l_recording_work


class test_l_recording_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_recording_work()

    def test__l_recording_work__instance(self):
        self.assertIsInstance(self.subject, l_recording_work)

    def test__l_recording_work__str(self):
        self.assertEqual(str(self.subject), 'L Recording Work')
