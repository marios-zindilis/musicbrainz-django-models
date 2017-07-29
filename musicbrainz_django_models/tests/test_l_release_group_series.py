from django.test import TestCase
from ..models import l_release_group_series


class test_l_release_group_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_release_group_series()

    def test__l_release_group_series__instance(self):
        self.assertIsInstance(self.subject, l_release_group_series)

    def test__l_release_group_series__str(self):
        self.assertEqual(str(self.subject), 'L Release Group Series')
