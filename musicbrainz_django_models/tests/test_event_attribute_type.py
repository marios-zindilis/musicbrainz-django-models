from django.test import TestCase
from ..models import event_attribute_type


class test_event_attribute_type(TestCase):
    def setUp(self):
        self.subject = event_attribute_type(name='Name')

    def test__event_attribute_type__instance(self):
        self.assertIsInstance(self.subject, event_attribute_type)

    def test__event_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
