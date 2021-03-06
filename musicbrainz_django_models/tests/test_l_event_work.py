from django.test import TestCase
from ..models import l_event_work


class test_l_event_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_work()

    def test__l_event_work__instance(self):
        self.assertIsInstance(self.subject, l_event_work)

    def test__l_event_work__str(self):
        self.assertEqual(str(self.subject), 'L Event Work')
