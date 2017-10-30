from django.test import TestCase
from ..models import work_attribute_type_allowed_value


class test_work_attribute_type_allowed_value(TestCase):
    def setUp(self):
        self.subject = work_attribute_type_allowed_value()

    def test__work_attribute_type_allowed_value__instance(self):
        self.assertIsInstance(self.subject, work_attribute_type_allowed_value)

    def test__work_attribute_type_allowed_value__str(self):
        self.assertEqual(str(self.subject), 'Work Attribute Type Allowed Value')
