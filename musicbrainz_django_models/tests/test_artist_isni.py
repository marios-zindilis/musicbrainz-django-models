from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_isni


class test_artist_isni(TestCase):
    def setUp(self):
        self.subject = artist_isni()
        self.ISNI = '1234567890123456'  # A valid ISNI.
        self.ISNI_TOO_SHORT = self.ISNI[:-1]
        self.ISNI_TOO_LONG = '{}X'.format(self.ISNI)

    def test__artist_isni__instance(self):
        self.assertIsInstance(self.subject, artist_isni)

    def test__artist_isni__str(self):
        self.subject.isni = self.ISNI
        self.assertEqual(str(self.subject), self.ISNI)

    def test__artist_isni__isni_too_short(self):
        self.subject.isni = self.ISNI_TOO_SHORT
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__artist_isni__isni_too_long(self):
        self.subject.isni = self.ISNI_TOO_LONG
        with self.assertRaises(ValidationError):
            self.subject.save()
