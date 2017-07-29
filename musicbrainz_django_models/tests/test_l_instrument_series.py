from django.test import TestCase
from ..models import l_instrument_series


class test_l_instrument_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_series()

    def test__l_instrument_series__instance(self):
        self.assertIsInstance(self.subject, l_instrument_series)

    def test__l_instrument_series__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Series')
