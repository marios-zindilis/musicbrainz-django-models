from django.test import TestCase
from ..models import l_event_url


class test_l_event_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_url()

    def test__l_event_url__instance(self):
        self.assertIsInstance(self.subject, l_event_url)

    def test__l_event_url__str(self):
        self.assertEqual(str(self.subject), 'L Event Url')
