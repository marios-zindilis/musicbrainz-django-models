from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import area_type


class test_area_type(TestCase):
    def setUp(self):
        self.subject = area_type(name='Country')

    def test__area_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__area_type__name_choise(self):
        self.subject = area_type(name="Invalid Type")
        with self.assertRaises(ValidationError):
            self.subject.save()
