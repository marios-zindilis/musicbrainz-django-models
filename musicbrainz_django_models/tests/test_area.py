from django.test import TestCase
from ..models import area_type, area


class test_area(TestCase):
    def test__area__instance(self):
        subject = area(name='Heaven')
        self.assertIsInstance(subject, area)

    def test__area__str(self):
        subject = area(name='Heaven')
        self.assertEqual(str(subject), subject.name)

    def test__area__unicode(self):
        subject = area(name='Hell')
        self.assertEqual(subject.__unicode__(), subject.name)

    def test__area__end_date_year(self):
        at = area_type(name='Country')
        at.save()
        subject = area(name='Utopia', end_date_year=2012, type=at)
        subject.save()
        self.assertTrue(subject.ended)

    def test__area__end_date_month(self):
        at = area_type(name='Country')
        at.save()
        subject = area(name='Fruitopia', end_date_month=12, type=at)
        subject.save()
        self.assertTrue(subject.ended)

    def test__area__end_date_day(self):
        at = area_type(name='Country')
        at.save()
        subject = area(name='Footopia', end_date_day=12, type=at)
        subject.save()
        self.assertTrue(subject.ended)
