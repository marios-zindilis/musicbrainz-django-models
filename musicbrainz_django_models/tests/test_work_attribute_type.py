from django.test import TestCase
from ..models import work_attribute_type


class test_work_attribute_type(TestCase):
    def setUp(self):
        self.subject = work_attribute_type(name='Name')

    def test__work_attribute_type__instance(self):
        self.assertIsInstance(self.subject, work_attribute_type)

    def test__work_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
