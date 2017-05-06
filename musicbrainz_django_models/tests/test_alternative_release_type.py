from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import alternative_release_type


class test_alternative_release_type(TestCase):
    def setUp(self):
        self.subject = alternative_release_type(name='Name')

    def test__alternative_release_type__instance(self):
        self.assertIsInstance(self.subject, alternative_release_type)

    def test__alternative_release_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__alternative_release_type__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
