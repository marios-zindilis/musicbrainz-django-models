from django.test import TestCase
from ..models import country_area
from ..models import area


class test_country_area(TestCase):
    def setUp(self):
        self.subject = country_area()
        self.subject_area = area(name='Somewhere')

    def test__country_area__instance(self):
        self.assertIsInstance(self.subject, country_area)

    def test__country_area__str(self):
        self.subject.area = self.subject_area
        self.assertEqual(str(self.subject), self.subject.area.name)
