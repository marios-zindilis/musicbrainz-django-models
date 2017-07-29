from django.test import TestCase
from ..models import l_instrument_url


class test_l_instrument_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_url()

    def test__l_instrument_url__instance(self):
        self.assertIsInstance(self.subject, l_instrument_url)

    def test__l_instrument_url__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Url')
