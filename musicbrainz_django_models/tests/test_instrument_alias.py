from django.test import TestCase
from ..models import instrument_alias
from ..models import instrument_alias_type
from ..models import instrument
import random


class test_instrument_alias(TestCase):
    def setUp(self):
        self.subject = instrument_alias(name='Name')
        # Set up an Instrument Alias Type:
        self.subject_instrument_alias_type = instrument_alias_type(
            name=random.choice(instrument_alias_type.NAME_CHOICES_LIST))
        self.subject_instrument_alias_type.save()
        # Set up an Instrument:
        self.subject_instrument = instrument()
        self.subject_instrument.save()

    def test__instrument_alias__instance(self):
        self.assertIsInstance(self.subject, instrument_alias)

    def test__instrument_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__instrument_alias__ended(self):
        self.assertFalse(self.subject.ended)

    def test__instrument_alias__end_date_year(self):
        self.subject.end_date_year = 2000
        self.subject.type = self.subject_instrument_alias_type
        self.subject.instrument = self.subject_instrument
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__instrument_alias__end_date_month(self):
        self.subject.end_date_month = 2
        self.subject.type = self.subject_instrument_alias_type
        self.subject.instrument = self.subject_instrument
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__instrument_alias__end_date_day(self):
        self.subject.end_date_year = 20
        self.subject.type = self.subject_instrument_alias_type
        self.subject.instrument = self.subject_instrument
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__instrument_alias__search_hint(self):
        instrument_alias_type_search_hint = instrument_alias_type(name=instrument_alias_type.SEARCH_HINT)
        instrument_alias_type_search_hint.save()
        self.subject.type = instrument_alias_type_search_hint
        self.subject.instrument = self.subject_instrument
        self.subject.sort_name = 'Some sort_name different to the name.'
        self.subject.locale = 'locale'
        self.subject.primary_for_locale = True
        self.subject.begin_date_year = 1234
        self.subject.begin_date_month = 12
        self.subject.begin_date_day = 1
        self.subject.end_date_year = 2000
        self.subject.end_date_month = 12
        self.subject.end_date_day = 3
        self.subject.save()

        self.assertEqual(self.subject.name, self.subject.sort_name)
        self.assertFalse(self.subject.primary_for_locale)
        self.assertIsNone(self.subject.locale)
        self.assertIsNone(self.subject.begin_date_year)
        self.assertIsNone(self.subject.begin_date_month)
        self.assertIsNone(self.subject.begin_date_day)
        self.assertIsNone(self.subject.end_date_year)
        self.assertIsNone(self.subject.end_date_month)
        self.assertIsNone(self.subject.end_date_day)
