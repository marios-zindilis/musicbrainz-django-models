from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import series_type


class test_series_type(TestCase):
    def setUp(self):
        self.subject = series_type(name='Name')

    def test__series_type__instance(self):
        self.assertIsInstance(self.subject, series_type)

    def test__series_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__series_type__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
