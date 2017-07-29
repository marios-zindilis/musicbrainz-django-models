from django.test import TestCase
from ..models import l_label_url


class test_l_label_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_url()

    def test__l_label_url__instance(self):
        self.assertIsInstance(self.subject, l_label_url)

    def test__l_label_url__str(self):
        self.assertEqual(str(self.subject), 'L Label Url')
