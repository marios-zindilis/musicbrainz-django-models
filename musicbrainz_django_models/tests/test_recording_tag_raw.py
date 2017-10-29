from django.test import TestCase
from ..models import recording_tag_raw


class test_recording_tag_raw(TestCase):
    def setUp(self):
        self.subject = recording_tag_raw()

    def test__recording_tag_raw__instance(self):
        self.assertIsInstance(self.subject, recording_tag_raw)

    def test__recording_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Recording Tag Raw')
