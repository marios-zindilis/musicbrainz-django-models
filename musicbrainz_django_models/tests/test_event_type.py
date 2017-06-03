from django.test import TestCase
from ..models import event_type


class test_event_type(TestCase):
    def setUp(self):
        self.subject = event_type(name='Name')

    def test__event_type__instance(self):
        self.assertIsInstance(self.subject, event_type)

    def test__event_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
