from django.test import TestCase
from ..models import area_alias
from ..models import area


class test_area_alias(TestCase):
    def setUp(self):
        self.subject = area_alias(name='Name')
        self.subject_area = area(name='Somewhere')
        self.subject_area.save()

    def test__area_alias__instance(self):
        self.assertIsInstance(self.subject, area_alias)

    def test__area_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__area_alias__ended(self):
        self.assertFalse(self.subject.ended)

    def test__area_alias__end_date_year(self):
        self.subject.end_date_year = 2000
        self.assertTrue(self.subject.ended)

    def test__area_alias__end_date_month(self):
        self.subject.end_date_month = 2
        self.assertTrue(self.subject.ended)

    def test__area_alias__end_date_day(self):
        self.subject.end_date_year = 20
        self.assertTrue(self.subject.ended)

    def test__area_alias__primary_for_locale(self):
        self.assertFalse(self.subject.primary_for_locale)

    def test__area_alias__primary_for_locale_without_locale(self):
        self.subject.locale = None
        self.subject.primary_for_locale = True
        self.subject.area = self.subject_area
        self.subject.save()
        self.assertFalse(self.subject.primary_for_locale)
