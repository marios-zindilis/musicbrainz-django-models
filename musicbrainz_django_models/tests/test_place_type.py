from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import place_type


class test_place_type(TestCase):
    def setUp(self):
        self.subject = place_type(name='Name')

    def test__place_type__instance(self):
        self.assertIsInstance(self.subject, place_type)

    def test__place_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__place_type__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
