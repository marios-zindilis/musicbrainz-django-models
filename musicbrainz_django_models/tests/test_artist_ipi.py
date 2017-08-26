from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_ipi


class test_artist_ipi(TestCase):
    def setUp(self):
        self.subject = artist_ipi()

    def test__artist_ipi__instance(self):
        self.assertIsInstance(self.subject, artist_ipi)

    def test__artist_ipi__str(self):
        self.subject.ipi = 12345678901
        self.assertEqual(str(self.subject), str(self.subject.ipi))

    def test__artist_ipi__empty_ipi(self):
        """Raises ValidationError if the IPI is empty."""
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__artist_ipi__ipi_too_short(self):
        self.subject.ipi = 1234567890
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__artist_ipi__ipi_too_long(self):
        self.subject.ipi = 123456789012
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__artist_ipi__ipi_not_numeric(self):
        self.subject.ipi = '1234567890A'
        with self.assertRaises(ValidationError):
            self.subject.save()
