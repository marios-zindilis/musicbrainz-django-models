from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import release_group_meta


class test_release_group_meta(TestCase):
    def setUp(self):
        self.subject = release_group_meta()

    def test__release_group_meta__instance(self):
        self.assertIsInstance(self.subject, release_group_meta)

    def test__release_group_meta__str(self):
        self.assertEqual(str(self.subject), 'Release Group Meta')

    def test__release_group_meta__rating_too_low(self):
        self.subject.rating = release_group_meta.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__release_group_meta__rating_too_high(self):
        self.subject.rating = release_group_meta.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
