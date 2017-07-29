from django.test import TestCase
from ..models import l_event_release


class test_l_event_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_event_release()

    def test__l_event_release__instance(self):
        self.assertIsInstance(self.subject, l_event_release)

    def test__l_event_release__str(self):
        self.assertEqual(str(self.subject), 'L Event Release')
