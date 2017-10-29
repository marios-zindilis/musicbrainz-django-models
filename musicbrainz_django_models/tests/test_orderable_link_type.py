from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import orderable_link_type


class test_orderable_link_type(TestCase):
    def setUp(self):
        self.subject = orderable_link_type()

    def test__orderable_link_type__instance(self):
        self.assertIsInstance(self.subject, orderable_link_type)

    def test__orderable_link_type__str(self):
        self.assertEqual(str(self.subject), 'Orderable Link Type')

    def test__orderable_link_type__direction_too_small(self):
        with self.assertRaises(ValidationError):
            self.subject.direction = orderable_link_type.DIRECTION_MIN - 1
            self.subject.save()

    def test__orderable_link_type__direction_too_big(self):
        with self.assertRaises(ValidationError):
            self.subject.direction = orderable_link_type.DIRECTION_MAX + 1
            self.subject.save()
