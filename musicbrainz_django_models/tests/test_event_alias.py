from django.test import TestCase
from ..models import event_alias
from ..models import event_alias_type
from ..models import event
import random


class test_event_alias(TestCase):
    def setUp(self):
        self.subject = event_alias(name='Name')
        # Set up an Event Alias Type:
        self.subject_event_alias_type = event_alias_type(name=random.choice(event_alias_type.NAME_CHOICES_LIST))
        self.subject_event_alias_type.save()
        # Set up an Event:
        self.subject_event = event()
        self.subject_event.save()

    def test__event_alias__instance(self):
        self.assertIsInstance(self.subject, event_alias)

    def test__event_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__event_alias__end_date_year(self):
        self.subject.type = self.subject_event_alias_type
        self.subject.event = self.subject_event
        self.subject.end_date_year = 1
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__event_alias__end_date_month(self):
        self.subject.type = self.subject_event_alias_type
        self.subject.event = self.subject_event
        self.subject.end_date_month = 1
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__event_alias__end_date_day(self):
        self.subject.type = self.subject_event_alias_type
        self.subject.event = self.subject_event
        self.subject.end_date_day = 1
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__event_alias__primary_for_locale(self):
        """
        When the `locale` is empty, `primary_for_locale` must be False when saved.
        """
        self.subject.type = self.subject_event_alias_type
        self.subject.event = self.subject_event
        self.subject.locale = None
        self.subject.primary_for_locale = True
        self.assertTrue(self.subject.primary_for_locale)
        self.subject.save()
        self.assertFalse(self.subject.primary_for_locale)

    def test__event_alias__search_hint(self):
        """
        When the `type` is `event_alias_type.SEARCH_HINT`, the `sort_name`
        must be equal to the `name`, `primary_for_locale` must be False,
        `locale` must be emtpy, and all the `*_date_*` fields must be empty.
        """

        event_alias_type_search_hint = event_alias_type(name=event_alias_type.SEARCH_HINT)
        event_alias_type_search_hint.save()
        self.subject.type = event_alias_type_search_hint
        self.subject.event = self.subject_event
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
