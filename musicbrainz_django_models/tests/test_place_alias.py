from django.test import TestCase
from ..models import place_alias
from ..models import place
from ..models import place_alias_type


class test_place_alias(TestCase):
    def setUp(self):
        self.subject = place_alias(name='Name')

        self.subject_place = place(name='Place')
        self.subject_place.save()

        self.subject_type = place_alias_type(name=place_alias_type.SEARCH_HINT)
        self.subject_type.save()

    def test__place_alias__instance(self):
        self.assertIsInstance(self.subject, place_alias)

    def test__place_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__place_alias__ended(self):
        self.subject.place = self.subject_place
        self.subject.type = self.subject_type
        self.subject.save()
        self.assertFalse(self.subject.ended)

    def test__place_alias__end_date_year(self):
        self.subject.type = self.subject_type
        self.subject.place = self.subject_place
        self.subject.end_date_year = 1212
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__place_alias__end_date_month(self):
        self.subject.type = self.subject_type
        self.subject.place = self.subject_place
        self.subject.end_date_month = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__place_alias__end_date_day(self):
        self.subject.place = self.subject_place
        self.subject.type = self.subject_type
        self.subject.end_date_day = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__place_alias__locale_is_none(self):
        self.subject.place = self.subject_place
        self.subject.type = self.subject_type
        self.subject.locale = None
        self.subject.save()
        self.assertFalse(self.subject.primary_for_locale)

    def test__place_alias__type_is_search_hint(self):
        self.subject.type = self.subject_type
        self.subject.place = self.subject_place
        self.subject.sort_name = 'This is the sort name'
        self.subject.begin_date_year = 1000
        self.subject.begin_date_month = 12
        self.subject.begin_date_day = 23
        self.subject.end_date_year = 1234
        self.subject.end_date_month = 1
        self.subject.end_date_day = 3
        self.subject.locale = 'Locale'
        self.subject.primary_for_locale = True
        self.subject.save()

        self.assertEquals(self.subject.name, self.subject.sort_name)
