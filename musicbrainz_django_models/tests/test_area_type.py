from django.test import TestCase
from ..models import area_type


class test_area_type(TestCase):
    def test_str(self):
        a = area_type(name='Country')
        self.assertEqual(str(a), a.name)

    def test_unicode(self):
        a = area_type(name='Country')
        self.assertEqual(a.__unicode__(), a.name)
