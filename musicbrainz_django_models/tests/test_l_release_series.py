from django.test import TestCase
from ..models import l_release_series


class test_l_release_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_release_series()

    def test__l_release_series__instance(self):
        self.assertIsInstance(self.subject, l_release_series)

    def test__l_release_series__str(self):
        self.assertEqual(str(self.subject), 'L Release Series')
