from django.test import TestCase
from ..models import event_tag_raw


class test_event_tag_raw(TestCase):
    def setUp(self):
        self.subject = event_tag_raw()

    def test__event_tag_raw__instance(self):
        self.assertIsInstance(self.subject, event_tag_raw)

    def test__event_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Event Tag Raw')
