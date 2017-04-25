from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import area_type


class test_area_type(TestCase):
    def test__area_type__str(self):
        subject = area_type(name='Country')
        self.assertEqual(str(subject), subject.name)

    def test__area_type__unicode(self):
        subject = area_type(name='Country')
        self.assertEqual(subject.__unicode__(), subject.name)

    def test__area_type__name_choise(self):
        subject = area_type(name="Invalid Type")
        with self.assertRaises(ValidationError):
            subject.save()
