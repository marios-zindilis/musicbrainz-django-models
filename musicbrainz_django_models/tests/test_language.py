from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import language


class test_language(TestCase):
    def setUp(self):
        self.subject = language(name='Greek')

    def test__language__instance(self):
        self.assertIsInstance(self.subject, language)

    def test__language__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__language__validation(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
