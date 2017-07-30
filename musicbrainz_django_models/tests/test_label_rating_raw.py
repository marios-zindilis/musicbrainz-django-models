from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import label_rating_raw


class test_label_rating_raw(TestCase):
    def setUp(self):
        self.subject = label_rating_raw()

    def test__label_rating_raw__instance(self):
        self.assertIsInstance(self.subject, label_rating_raw)

    def test__label_rating_raw__str(self):
        self.assertEqual(str(self.subject), 'Label Rating Raw')

    def test__label_rating_raw__rating_min_value(self):
        self.subject.rating = label_rating_raw.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__label_rating_raw__rating_max_value(self):
        self.subject.rating = label_rating_raw.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
