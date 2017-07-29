from django.test import TestCase
from ..models import l_event_recording


class test_l_event_recording(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_recording()

    def test__l_event_recording__instance(self):
        self.assertIsInstance(self.subject, l_event_recording)

    def test__l_event_recording__str(self):
        self.assertEqual(str(self.subject), 'L Event Recording')
