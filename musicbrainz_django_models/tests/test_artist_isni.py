from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_isni


class test_artist_isni(TestCase):
    def test__artist_isni__str(self):
        subject = artist_isni(isni='1234567890123456')
        self.assertEqual(str(subject), subject.isni)

    def test__artist_isni__isni_too_short(self):
        subject = artist_isni(isni='12345678901235')
        with self.assertRaises(ValidationError):
            subject.save()

    def test__artist_isni__isni_too_long(self):
        subject = artist_isni(isni='12345678901234567')
        with self.assertRaises(ValidationError):
            subject.save()
