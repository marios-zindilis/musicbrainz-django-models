from django.test import TestCase
from ..models import label_attribute_type


class test_label_attribute_type(TestCase):
    def setUp(self):
        self.subject = label_attribute_type(name='Name')

    def test__label_attribute_type__instance(self):
        self.assertIsInstance(self.subject, label_attribute_type)

    def test__label_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
