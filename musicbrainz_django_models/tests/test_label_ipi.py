from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import label_ipi


class test_label_ipi(TestCase):
    def setUp(self):
        self.subject = label_ipi()

    def test__label_ipi__instance(self):
        self.assertIsInstance(self.subject, label_ipi)

    def test__label_ipi__str(self):
        self.subject.ipi = 12345678901
        self.assertEqual(str(self.subject), str(self.subject.ipi))

    def test__label_ipi__empty_ipi(self):
        """Raises ValidationError if the IPI is empty."""
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__label_ipi__ipi_too_short(self):
        """Raises ValidationError if the IPI is shorter that 11 characters."""
        self.subject.ipi = 1234567890
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__label_ipi__ipi_too_long(self):
        """Raises ValidationError if the IPI is longer that 11 characters."""
        self.subject.ipi = 123456789012
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__label_ipi__ipi_not_numeric(self):
        """Raises ValidationError if the IPI is not numeric."""
        self.subject.ipi = '1234567890A'
        with self.assertRaises(ValidationError):
            self.subject.save()
