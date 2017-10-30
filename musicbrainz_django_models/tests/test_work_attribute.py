from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import work_attribute


class test_work_attribute(TestCase):
    def setUp(self):
        self.subject = work_attribute()

    def test__work_attribute__instance(self):
        self.assertIsInstance(self.subject, work_attribute)

    def test__work_attribute__str(self):
        self.assertEqual(str(self.subject), 'Work Attribute')

    def test__work_attribute__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
