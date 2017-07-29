from django.test import TestCase
from ..models import l_place_series


class test_l_place_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_place_series()

    def test__l_place_series__instance(self):
        self.assertIsInstance(self.subject, l_place_series)

    def test__l_place_series__str(self):
        self.assertEqual(str(self.subject), 'L Place Series')
