from django.test import TestCase
from ..models import label_alias
from ..models import label
from ..models import label_alias_type


class test_label_alias(TestCase):
    def setUp(self):
        self.subject = label_alias(name='Name')

        self.subject_label = label(name='Label')
        self.subject_label.save()

        self.subject_type = label_alias_type(name=label_alias_type.SEARCH_HINT)
        self.subject_type.save()

    def test__label_alias__instance(self):
        self.assertIsInstance(self.subject, label_alias)

    def test__label_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__label_alias__ended(self):
        self.subject.label = self.subject_label
        self.subject.save()
        self.assertFalse(self.subject.ended)

    def test__label_alias__end_date_year(self):
        self.subject.label = self.subject_label
        self.subject.end_date_year = 1212
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__label_alias__end_date_month(self):
        self.subject.label = self.subject_label
        self.subject.end_date_month = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__label_alias__end_date_day(self):
        self.subject.label = self.subject_label
        self.subject.end_date_day = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__label_alias__locale_is_none(self):
        self.subject.label = self.subject_label
        self.subject.locale = None
        self.subject.save()
        self.assertFalse(self.subject.primary_for_locale)

    def test__label_alias__type_is_search_hint(self):
        self.subject.type = self.subject_type
        self.subject.label = self.subject_label
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
