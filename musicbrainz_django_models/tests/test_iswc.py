from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import iswc


class test_iswc(TestCase):
    def setUp(self):
        self.subject = iswc(iswc='ISWC')

    def test__iswc__instance(self):
        self.assertIsInstance(self.subject, iswc)

    def test__iswc__str(self):
        self.assertEqual(str(self.subject), self.subject.iswc)

    def test__iswc__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
