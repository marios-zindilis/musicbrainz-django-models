from django.test import TestCase
from ..models import place_attribute_type


class test_place_attribute_type(TestCase):
    def setUp(self):
        self.subject = place_attribute_type(name='Name')

    def test__place_attribute_type__instance(self):
        self.assertIsInstance(self.subject, place_attribute_type)

    def test__place_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
