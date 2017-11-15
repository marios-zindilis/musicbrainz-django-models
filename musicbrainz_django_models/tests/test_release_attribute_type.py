from django.test import TestCase
from ..models import release_attribute_type


class test_release_attribute_type(TestCase):
    def setUp(self):
        self.subject = release_attribute_type(name='Name')

    def test__release_attribute_type__instance(self):
        self.assertIsInstance(self.subject, release_attribute_type)

    def test__release_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
