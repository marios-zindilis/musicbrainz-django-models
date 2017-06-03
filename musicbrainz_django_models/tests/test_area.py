from django.test import TestCase
from ..models import area


class test_area(TestCase):
    def setUp(self):
        self.subject = area(name='Heaven')

    def test__area__instance(self):
        self.assertIsInstance(self.subject, area)

    def test__area__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__area__ended(self):
        self.assertFalse(self.subject.ended)

    def test__area__end_date_year(self):
        self.subject.end_date_year = 2012
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__area__end_date_month(self):
        self.subject.end_date_month = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__area__end_date_day(self):
        self.subject.end_date_day = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)
