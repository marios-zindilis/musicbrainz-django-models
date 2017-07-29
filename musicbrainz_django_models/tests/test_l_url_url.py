from django.test import TestCase
from ..models import l_url_url


class test_l_url_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_url_url()

    def test__l_url_url__instance(self):
        self.assertIsInstance(self.subject, l_url_url)

    def test__l_url_url__str(self):
        self.assertEqual(str(self.subject), 'L Url Url')
