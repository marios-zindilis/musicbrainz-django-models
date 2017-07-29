from django.test import TestCase
from ..models import l_area_label


class test_l_area_label(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_label()

    def test__l_area_label__instance(self):
        self.assertIsInstance(self.subject, l_area_label)

    def test__l_area_label__str(self):
        self.assertEqual(str(self.subject), 'L Area Label')
