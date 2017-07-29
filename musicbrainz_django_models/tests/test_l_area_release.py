from django.test import TestCase
from ..models import l_area_release


class test_l_area_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_release()

    def test__l_area_release__instance(self):
        self.assertIsInstance(self.subject, l_area_release)

    def test__l_area_release__str(self):
        self.assertEqual(str(self.subject), 'L Area Release')
