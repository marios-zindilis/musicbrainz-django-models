from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_ipi


class test_artist_ipi(TestCase):
    def test__artist_ipi__str(self):
        subject = artist_ipi(ipi=12345678901)
        self.assertEqual(str(subject), str(subject.ipi))

    def test__artist_ipi__unicode(self):
        subject = artist_ipi(ipi=12345678901)
        self.assertEqual(subject.__unicode__(), str(subject.ipi))

    def test__artist_ipi__ipi_too_short(self):
        subject = artist_ipi(ipi=1234567890)
        with self.assertRaises(ValidationError):
            subject.save()

    def test__artist_ipi__ipi_too_long(self):
        subject = artist_ipi(ipi=123456789012)
        with self.assertRaises(ValidationError):
            subject.save()
