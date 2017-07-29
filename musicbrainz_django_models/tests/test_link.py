from django.test import TestCase
from ..models import link
from ..models import link_type


class test_link(TestCase):
    def setUp(self):
        self.subject = link()
        self.subject_link_type = link_type(name='Link Type')
        self.subject_link_type.save()

    def test__link__instance(self):
        self.assertIsInstance(self.subject, link)

    def test__link__str(self):
        self.assertEqual(str(self.subject), 'Link')

    def test__link__ended(self):
        self.assertFalse(self.subject.ended)

    def test__link__end_date_year(self):
        self.subject.end_date_year = 2012
        self.subject.link_type = self.subject_link_type
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__link__end_date_month(self):
        self.subject.end_date_month = 12
        self.subject.link_type = self.subject_link_type
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__link__end_date_day(self):
        self.subject.end_date_day = 12
        self.subject.link_type = self.subject_link_type
        self.subject.save()
        self.assertTrue(self.subject.ended)
