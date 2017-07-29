from django.test import TestCase
from ..models import l_area_url


class test_l_area_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_url()

    def test__l_area_url__instance(self):
        self.assertIsInstance(self.subject, l_area_url)

    def test__l_area_url__str(self):
        self.assertEqual(str(self.subject), 'L Area Url')
