from django.test import TestCase
from ..models import l_label_series


class test_l_label_series(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_series()

    def test__l_label_series__instance(self):
        self.assertIsInstance(self.subject, l_label_series)

    def test__l_label_series__str(self):
        self.assertEqual(str(self.subject), 'L Label Series')
