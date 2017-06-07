from django.test import TestCase
from ..models import place
from ..models import place_type
from ..models import area
import random


class test_place(TestCase):
    def setUp(self):
        self.subject = place(name='Name')
        self.subject_area = area(name='Somewhere')
        self.subject_area.save()
        self.subject_place_type = place_type(name=random.choice(place_type.NAME_CHOICES_LIST))
        self.subject_place_type.save()

    def test__place__instance(self):
        self.assertIsInstance(self.subject, place)

    def test__place__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__place__end_date_year(self):
        self.subject.area = self.subject_area
        self.subject.type = self.subject_place_type
        self.subject.end_date_year = 2012
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__place__end_date_month(self):
        self.subject.area = self.subject_area
        self.subject.type = self.subject_place_type
        self.subject.end_date_month = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__place__end_date_day(self):
        self.subject.area = self.subject_area
        self.subject.type = self.subject_place_type
        self.subject.end_date_day = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)
