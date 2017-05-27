from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_meta


class test_artist_meta(TestCase):
    def setUp(self):
        self.subject = artist_meta()

    def test__artist_meta__instance(self):
        self.assertIsInstance(self.subject, artist_meta)

    def test__artist_meta__str(self):
        self.assertEqual(str(self.subject), 'Artist Meta')

    def test__artist_meta__rating_min_value(self):
        self.subject.rating = artist_meta.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__artist_meta__rating_max_value(self):
        self.subject.rating = artist_meta.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
