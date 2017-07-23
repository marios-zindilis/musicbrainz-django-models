from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import instrument_alias_type


class test_instrument_alias_type(TestCase):
    def setUp(self):
        self.subject = instrument_alias_type(name='Name')

    def test__instrument_alias_type__instance(self):
        self.assertIsInstance(self.subject, instrument_alias_type)

    def test__instrument_alias_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__instrument_alias_type__name(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
