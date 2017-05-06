from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import release_status


class test_release_status(TestCase):
    def setUp(self):
        self.subject = release_status(name='Name')

    def test__release_status__instance(self):
        self.assertIsInstance(self.subject, release_status)

    def test__release_status__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__release_status__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
