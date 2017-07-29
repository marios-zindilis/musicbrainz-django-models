from django.test import TestCase
from ..models import l_place_work


class test_l_place_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_place_work()

    def test__l_place_work__instance(self):
        self.assertIsInstance(self.subject, l_place_work)

    def test__l_place_work__str(self):
        self.assertEqual(str(self.subject), 'L Place Work')
