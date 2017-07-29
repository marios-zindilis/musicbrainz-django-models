from django.test import TestCase
from ..models import l_instrument_release


class test_l_instrument_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_release()

    def test__l_instrument_release__instance(self):
        self.assertIsInstance(self.subject, l_instrument_release)

    def test__l_instrument_release__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Release')
