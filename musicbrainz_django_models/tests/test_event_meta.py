from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import event_meta


class test_event_meta(TestCase):
    def setUp(self):
        self.subject = event_meta()

    def test__event_meta__instance(self):
        self.assertIsInstance(self.subject, event_meta)

    def test__event_meta__str(self):
        self.assertEqual(str(self.subject), 'Event Meta')

    def test__event_meta__rating_min_value(self):
        self.subject.rating = event_meta.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__event_meta__rating_max_value(self):
        self.subject.rating = event_meta.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
