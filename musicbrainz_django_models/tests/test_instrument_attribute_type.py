from django.test import TestCase
from ..models import instrument_attribute_type


class test_instrument_attribute_type(TestCase):
    def setUp(self):
        self.subject = instrument_attribute_type(name='Name')

    def test__instrument_attribute_type__instance(self):
        self.assertIsInstance(self.subject, instrument_attribute_type)

    def test__instrument_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
