from django.test import TestCase
from ..models import l_instrument_recording


class test_l_instrument_recording(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_recording()

    def test__l_instrument_recording__instance(self):
        self.assertIsInstance(self.subject, l_instrument_recording)

    def test__l_instrument_recording__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Recording')
