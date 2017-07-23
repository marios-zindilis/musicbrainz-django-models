from django.test import TestCase
from ..models import event_annotation


class test_event_annotation(TestCase):
    def setUp(self):
        self.subject = event_annotation()

    def test__event_annotation__instance(self):
        self.assertIsInstance(self.subject, event_annotation)

    def test__event_annotation__str(self):
        self.assertEqual(str(self.subject), 'Event Annotation')
