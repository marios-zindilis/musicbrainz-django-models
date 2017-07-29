from django.test import TestCase
from ..models import l_instrument_instrument


class test_l_instrument_instrument(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_instrument()

    def test__l_instrument_instrument__instance(self):
        self.assertIsInstance(self.subject, l_instrument_instrument)

    def test__l_instrument_instrument__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Instrument')
