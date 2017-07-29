from django.test import TestCase
from ..models import l_artist_label


class test_l_artist_label(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_label()

    def test__l_artist_label__instance(self):
        self.assertIsInstance(self.subject, l_artist_label)

    def test__l_artist_label__str(self):
        self.assertEqual(str(self.subject), 'L Artist Label')
