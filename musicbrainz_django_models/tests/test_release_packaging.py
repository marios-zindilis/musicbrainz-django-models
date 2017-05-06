from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import release_packaging


class test_release_packaging(TestCase):
    def setUp(self):
        self.subject = release_packaging(name='Name')

    def test__release_packaging__instance(self):
        self.assertIsInstance(self.subject, release_packaging)

    def test__release_packaging__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__release_packaging__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
