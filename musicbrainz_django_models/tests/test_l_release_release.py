from django.test import TestCase
from ..models import l_release_release


class test_l_release_release(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_release_release()

    def test__l_release_release__instance(self):
        self.assertIsInstance(self.subject, l_release_release)

    def test__l_release_release__str(self):
        self.assertEqual(str(self.subject), 'L Release Release')
