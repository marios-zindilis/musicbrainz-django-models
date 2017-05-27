from django.test import TestCase
from ..models import area_alias_type


class test_area_alias_type(TestCase):
    def setUp(self):
        self.subject = area_alias_type(name='Name')

    def test__area_alias_type__instance(self):
        self.assertIsInstance(self.subject, area_alias_type)

    def test__area_alias_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
