from django.test import TestCase
from ..models import l_label_label


class test_l_label_label(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_label()

    def test__l_label_label__instance(self):
        self.assertIsInstance(self.subject, l_label_label)

    def test__l_label_label__str(self):
        self.assertEqual(str(self.subject), 'L Label Label')
