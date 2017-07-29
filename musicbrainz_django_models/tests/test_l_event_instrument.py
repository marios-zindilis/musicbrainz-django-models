from django.test import TestCase
from ..models import l_event_instrument


class test_l_event_instrument(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_instrument()

    def test__l_event_instrument__instance(self):
        self.assertIsInstance(self.subject, l_event_instrument)

    def test__l_event_instrument__str(self):
        self.assertEqual(str(self.subject), 'L Event Instrument')
