from django.test import TestCase
from ..models import event
from ..models import event_type


class test_event(TestCase):
    def setUp(self):
        self.subject = event(name='Name')
        self.subject_event_type = event_type(name='Event Type')
        self.subject_event_type.save()

    def test__event__instance(self):
        self.assertIsInstance(self.subject, event)

    def test__event__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__event__ended(self):
        self.assertFalse(self.subject.ended)

    def test__event__end_date_year(self):
        self.subject.end_date_year = 2012
        self.subject.type = self.subject_event_type
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__event__end_date_month(self):
        self.subject.end_date_month = 12
        self.subject.type = self.subject_event_type
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__event__end_date_day(self):
        self.subject.end_date_day = 12
        self.subject.type = self.subject_event_type
        self.subject.save()
        self.assertTrue(self.subject.ended)
