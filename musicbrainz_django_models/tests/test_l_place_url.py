from django.test import TestCase
from ..models import l_place_url


class test_l_place_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_place_url()

    def test__l_place_url__instance(self):
        self.assertIsInstance(self.subject, l_place_url)

    def test__l_place_url__str(self):
        self.assertEqual(str(self.subject), 'L Place Url')
