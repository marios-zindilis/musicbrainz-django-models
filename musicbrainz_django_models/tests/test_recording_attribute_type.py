from django.test import TestCase
from ..models import recording_attribute_type


class test_recording_attribute_type(TestCase):
    def setUp(self):
        self.subject = recording_attribute_type(name='Name')

    def test__recording_attribute_type__instance(self):
        self.assertIsInstance(self.subject, recording_attribute_type)

    def test__recording_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
