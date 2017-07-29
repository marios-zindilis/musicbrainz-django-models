from django.test import TestCase
from ..models import l_instrument_work


class test_l_instrument_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_instrument_work()

    def test__l_instrument_work__instance(self):
        self.assertIsInstance(self.subject, l_instrument_work)

    def test__l_instrument_work__str(self):
        self.assertEqual(str(self.subject), 'L Instrument Work')
