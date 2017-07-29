from django.test import TestCase
from ..models import l_series_url


class test_l_series_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_series_url()

    def test__l_series_url__instance(self):
        self.assertIsInstance(self.subject, l_series_url)

    def test__l_series_url__str(self):
        self.assertEqual(str(self.subject), 'L Series Url')
