from django.test import TestCase
from ..models import l_artist_event


class test_l_artist_event(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_event()

    def test__l_artist_event__instance(self):
        self.assertIsInstance(self.subject, l_artist_event)

    def test__l_artist_event__str(self):
        self.assertEqual(str(self.subject), 'L Artist Event')
