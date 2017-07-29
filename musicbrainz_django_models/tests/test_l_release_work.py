from django.test import TestCase
from ..models import l_release_work


class test_l_release_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_release_work()

    def test__l_release_work__instance(self):
        self.assertIsInstance(self.subject, l_release_work)

    def test__l_release_work__str(self):
        self.assertEqual(str(self.subject), 'L Release Work')
