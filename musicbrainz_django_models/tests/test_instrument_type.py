from django.test import TestCase
from ..models import instrument_type


class test_instrument_type(TestCase):
    def test__instrument_type__instance(self):
        subject = instrument_type(name='String')
        self.assertIsInstance(subject, instrument_type)

    def test__instrument_type__str(self):
        subject = instrument_type(name='Wind')
        self.assertEquals(str(subject), subject.name)

    def test__instrument_type__unicode(self):
        subject = instrument_type(name='Percussion')
        self.assertEquals(subject.__unicode__(), subject.name)
