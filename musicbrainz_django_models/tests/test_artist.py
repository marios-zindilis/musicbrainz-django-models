from django.test import TestCase
from ..models import artist


class test_artist(TestCase):
    def test__artist__str(self):
        subject = artist(name='Bob Squarepants')
        self.assertEqual(str(subject), subject.name)

    def test__artist__end_date_year(self):
        subject = artist(name='Bob Squarepants', end_date_year=1)
        subject.save()
        self.assertTrue(subject.ended)

    def test__artist__end_date_month(self):
        subject = artist(name='Bob Squarepants', end_date_month=1)
        subject.save()
        self.assertTrue(subject.ended)

    def test__artist__end_date_day(self):
        subject = artist(name='Bob Squarepants', end_date_day=1)
        subject.save()
        self.assertTrue(subject.ended)
