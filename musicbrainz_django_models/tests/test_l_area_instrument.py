from django.test import TestCase
from ..models import l_area_instrument


class test_l_area_instrument(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_instrument()

    def test__l_area_instrument__instance(self):
        self.assertIsInstance(self.subject, l_area_instrument)

    def test__l_area_instrument__str(self):
        self.assertEqual(str(self.subject), 'L Area Instrument')
