from django.test import TestCase
from ..models import l_place_release


class test_l_place_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_place_release()

    def test__l_place_release__instance(self):
        self.assertIsInstance(self.subject, l_place_release)

    def test__l_place_release__str(self):
        self.assertEqual(str(self.subject), 'L Place Release')
