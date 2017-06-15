from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import event_alias_type


class test_event_alias_type(TestCase):
    def setUp(self):
        self.subject = event_alias_type(name='Name')

    def test__event_alias_type__instance(self):
        self.assertIsInstance(self.subject, event_alias_type)

    def test__event_alias_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__event_alias_type__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
