from django.test import TestCase
from ..models import event_tag


class test_event_tag(TestCase):
    def setUp(self):
        self.subject = event_tag()

    def test__event_tag__instance(self):
        self.assertIsInstance(self.subject, event_tag)

    def test__event_tag__str(self):
        self.assertEqual(str(self.subject), 'Event Tag')
