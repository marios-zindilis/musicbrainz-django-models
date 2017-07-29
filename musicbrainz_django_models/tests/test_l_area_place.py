from django.test import TestCase
from ..models import l_area_place


class test_l_area_place(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_place()

    def test__l_area_place__instance(self):
        self.assertIsInstance(self.subject, l_area_place)

    def test__l_area_place__str(self):
        self.assertEqual(str(self.subject), 'L Area Place')
