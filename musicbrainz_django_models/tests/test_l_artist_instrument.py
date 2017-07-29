from django.test import TestCase
from ..models import l_artist_instrument


class test_l_artist_instrument(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_artist_instrument()

    def test__l_artist_instrument__instance(self):
        self.assertIsInstance(self.subject, l_artist_instrument)

    def test__l_artist_instrument__str(self):
        self.assertEqual(str(self.subject), 'L Artist Instrument')
