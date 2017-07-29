from django.test import TestCase
from ..models import l_event_series


class test_l_event_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_series()

    def test__l_event_series__instance(self):
        self.assertIsInstance(self.subject, l_event_series)

    def test__l_event_series__str(self):
        self.assertEqual(str(self.subject), 'L Event Series')
