from django.test import TestCase
from ..models import medium_attribute_type_allowed_value_allowed_format


class test_medium_attribute_type_allowed_value_allowed_format(TestCase):
    def setUp(self):
        self.subject = medium_attribute_type_allowed_value_allowed_format()

    def test__medium_attribute_type_allowed_value_allowed_format__instance(self):
        self.assertIsInstance(self.subject, medium_attribute_type_allowed_value_allowed_format)

    def test__medium_attribute_type_allowed_value_allowed_format__str(self):
        self.assertEqual(str(self.subject), 'Medium Attribute Type Allowed Value Allowed Format')
