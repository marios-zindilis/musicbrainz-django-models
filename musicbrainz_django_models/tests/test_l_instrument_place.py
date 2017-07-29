from django.test import TestCase
from ..models import l_instrument_place


class test_l_instrument_place(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_place()

    def test__l_instrument_place__instance(self):
        self.assertIsInstance(self.subject, l_instrument_place)

    def test__l_instrument_place__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Place')
