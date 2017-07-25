from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import isrc


class test_isrc(TestCase):
    def setUp(self):
        self.subject = isrc(isrc='ISRC')

    def test__isrc__instance(self):
        self.assertIsInstance(self.subject, isrc)

    def test__isrc__str(self):
        self.assertEqual(str(self.subject), self.subject.isrc)

    def test__isrc__isrc(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
