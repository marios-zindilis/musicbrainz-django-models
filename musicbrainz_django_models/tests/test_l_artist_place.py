from django.test import TestCase
from ..models import l_artist_place


class test_l_artist_place(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_place()

    def test__l_artist_place__instance(self):
        self.assertIsInstance(self.subject, l_artist_place)

    def test__l_artist_place__str(self):
        self.assertEqual(str(self.subject), 'L Artist Place')
