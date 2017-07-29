from django.test import TestCase
from ..models import l_area_area


class test_l_area_area(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_area()

    def test__l_area_area__instance(self):
        self.assertIsInstance(self.subject, l_area_area)

    def test__l_area_area__str(self):
        self.assertEqual(str(self.subject), 'L Area Area')
