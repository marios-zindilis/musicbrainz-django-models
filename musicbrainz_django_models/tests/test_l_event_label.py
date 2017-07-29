from django.test import TestCase
from ..models import l_event_label


class test_l_event_label(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_label()

    def test__l_event_label__instance(self):
        self.assertIsInstance(self.subject, l_event_label)

    def test__l_event_label__str(self):
        self.assertEqual(str(self.subject), 'L Event Label')
