from django.test import TestCase
from ..models import track_raw


class test_track_raw(TestCase):
    def setUp(self):
        self.subject = track_raw()

    def test__track_raw__instance(self):
        self.assertIsInstance(self.subject, track_raw)

    def test__track_raw__str(self):
        self.assertEqual(str(self.subject), 'Track Raw')
