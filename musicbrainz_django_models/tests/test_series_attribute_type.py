from django.test import TestCase
from ..models import series_attribute_type


class test_series_attribute_type(TestCase):
    def setUp(self):
        self.subject = series_attribute_type(name='Name')

    def test__series_attribute_type__instance(self):
        self.assertIsInstance(self.subject, series_attribute_type)

    def test__series_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
