from django.test import TestCase
from ..models import l_instrument_label


class test_l_instrument_label(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_label()

    def test__l_instrument_label__instance(self):
        self.assertIsInstance(self.subject, l_instrument_label)

    def test__l_instrument_label__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Label')
