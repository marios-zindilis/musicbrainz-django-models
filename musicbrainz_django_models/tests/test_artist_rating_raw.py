from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_rating_raw


class test_artist_rating_raw(TestCase):
    def setUp(self):
        self.subject = artist_rating_raw()

    def test__artist_rating_raw__instance(self):
        self.assertIsInstance(self.subject, artist_rating_raw)

    def test__artist_rating_raw__str(self):
        self.assertEqual(str(self.subject), 'Artist Rating Raw')

    def test__artist_rating_raw__rating_min_value(self):
        self.subject.rating = artist_rating_raw.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__artist_rating_raw__rating_max_value(self):
        self.subject.rating = artist_rating_raw.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
