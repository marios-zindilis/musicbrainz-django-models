from django.test import TestCase
from ..models import recording_alias


class test_recording_alias(TestCase):
    def setUp(self):
        self.subject = recording_alias()

    def test__recording_alias__instance(self):
        self.assertIsInstance(self.subject, recording_alias)

    def test__recording_alias__str(self):
        self.assertEqual(str(self.subject), 'Recording Alias')
