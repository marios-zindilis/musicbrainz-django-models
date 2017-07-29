from django.test import TestCase
from ..models import l_area_artist


class test_l_area_artist(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_artist()

    def test__l_area_artist__instance(self):
        self.assertIsInstance(self.subject, l_area_artist)

    def test__l_area_artist__str(self):
        self.assertEqual(str(self.subject), 'L Area Artist')
