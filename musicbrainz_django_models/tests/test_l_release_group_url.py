from django.test import TestCase
from ..models import l_release_group_url


class test_l_release_group_url(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_release_group_url()

    def test__l_release_group_url__instance(self):
        self.assertIsInstance(self.subject, l_release_group_url)

    def test__l_release_group_url__str(self):
        self.assertEqual(str(self.subject), 'L Release Group Url')
