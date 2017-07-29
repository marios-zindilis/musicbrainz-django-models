from django.test import TestCase
from ..models import l_label_release


class test_l_label_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_release()

    def test__l_label_release__instance(self):
        self.assertIsInstance(self.subject, l_label_release)

    def test__l_label_release__str(self):
        self.assertEqual(str(self.subject), 'L Label Release')
