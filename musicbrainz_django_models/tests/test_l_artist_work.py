from django.test import TestCase
from ..models import l_artist_work


class test_l_artist_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_work()

    def test__l_artist_work__instance(self):
        self.assertIsInstance(self.subject, l_artist_work)

    def test__l_artist_work__str(self):
        self.assertEqual(str(self.subject), 'L Artist Work')
