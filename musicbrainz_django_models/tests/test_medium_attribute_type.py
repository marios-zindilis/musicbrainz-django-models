from django.test import TestCase
from ..models import medium_attribute_type


class test_medium_attribute_type(TestCase):
    def setUp(self):
        self.subject = medium_attribute_type(name='Name')

    def test__medium_attribute_type__instance(self):
        self.assertIsInstance(self.subject, medium_attribute_type)

    def test__medium_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
