from django.test import TestCase
from ..models import l_event_place


class test_l_event_place(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_place()

    def test__l_event_place__instance(self):
        self.assertIsInstance(self.subject, l_event_place)

    def test__l_event_place__str(self):
        self.assertEqual(str(self.subject), 'L Event Place')
