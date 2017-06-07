from django.test import TestCase
from ..models import link_attribute_type


class test_link_attribute_type(TestCase):
    def setUp(self):
        self.subject = link_attribute_type(name='Name')

    def test__link_attribute_type__instance(self):
        self.assertIsInstance(self.subject, link_attribute_type)

    def test__link_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
