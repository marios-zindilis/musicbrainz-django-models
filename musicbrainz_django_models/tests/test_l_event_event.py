from django.test import TestCase
from ..models import l_event_event


class test_l_event_event(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_event()

    def test__l_event_event__instance(self):
        self.assertIsInstance(self.subject, l_event_event)

    def test__l_event_event__str(self):
        self.assertEqual(str(self.subject), 'L Event Event')
