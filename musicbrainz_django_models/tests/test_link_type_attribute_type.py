from django.test import TestCase
from ..models import link_type_attribute_type


class test_link_type_attribute_type(TestCase):
    def setUp(self):
        self.subject = link_type_attribute_type()

    def test__link_type_attribute_type__instance(self):
        self.assertIsInstance(self.subject, link_type_attribute_type)

    def test__link_type_attribute_type__str(self):
        self.assertEqual(str(self.subject), 'Link Type Attribute Type')
