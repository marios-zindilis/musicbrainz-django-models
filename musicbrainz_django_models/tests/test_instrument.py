from django.test import TestCase
from ..models import instrument


class test_instrument(TestCase):
    def test__instrument__instance(self):
        subject = instrument(name='Guitar')
        self.assertIsInstance(subject, instrument)

    def test__instrument__str(self):
        subject = instrument(name='Piano')
        self.assertEquals(str(subject), subject.name)
