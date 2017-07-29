from django.test import TestCase
from ..models import l_area_series


class test_l_area_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_series()

    def test__l_area_series__instance(self):
        self.assertIsInstance(self.subject, l_area_series)

    def test__l_area_series__str(self):
        self.assertEqual(str(self.subject), 'L Area Series')
