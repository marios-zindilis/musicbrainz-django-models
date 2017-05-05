from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import label_type


class test_label_type(TestCase):
    def setUp(self):
        self.subject = label_type(name='Name')

    def test__label_type__instance(self):
        self.assertIsInstance(self.subject, label_type)

    def test__label_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__label_type__unicode(self):
        self.assertEqual(self.subject.__unicode__(), self.subject.name)

    def test__label_type__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
