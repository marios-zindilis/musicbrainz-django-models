from django.test import TestCase
from ..models import label_alias_type


class test_label_alias_type(TestCase):
    def setUp(self):
        self.subject = label_alias_type(name='Name')

    def test__label_alias_type__instance(self):
        self.assertIsInstance(self.subject, label_alias_type)

    def test__label_alias_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
