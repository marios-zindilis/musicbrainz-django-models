from django.test import TestCase
from ..models import l_series_series


class test_l_series_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_series_series()

    def test__l_series_series__instance(self):
        self.assertIsInstance(self.subject, l_series_series)

    def test__l_series_series__str(self):
        self.assertEqual(str(self.subject), 'L Series Series')
