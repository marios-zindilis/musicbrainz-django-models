from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import label


class test_label(TestCase):
    def setUp(self):
        self.subject = label(name='Name')

    def test__label__instance(self):
        self.assertIsInstance(self.subject, label)

    def test__label__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__label__end_date_year(self):
        self.subject.end_date_year = 2012
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__label__end_date_month(self):
        self.subject.end_date_month = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__label__end_date_day(self):
        self.subject.end_date_day = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__label__label_code_min_value(self):
        self.subject.label_code = label.LABEL_CODE_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__label__label_code_max_value(self):
        self.subject.label_code = label.LABEL_CODE_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
