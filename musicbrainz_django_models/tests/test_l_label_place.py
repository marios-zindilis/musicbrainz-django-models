from django.test import TestCase
from ..models import l_label_place


class test_l_label_place(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_place()

    def test__l_label_place__instance(self):
        self.assertIsInstance(self.subject, l_label_place)

    def test__l_label_place__str(self):
        self.assertEqual(str(self.subject), 'L Label Place')
