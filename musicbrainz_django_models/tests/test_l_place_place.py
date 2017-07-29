from django.test import TestCase
from ..models import l_place_place


class test_l_place_place(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_place_place()

    def test__l_place_place__instance(self):
        self.assertIsInstance(self.subject, l_place_place)

    def test__l_place_place__str(self):
        self.assertEqual(str(self.subject), 'L Place Place')
