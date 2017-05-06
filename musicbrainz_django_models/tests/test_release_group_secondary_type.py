from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import release_group_secondary_type


class test_release_group_secondary_type(TestCase):
    def setUp(self):
        self.subject = release_group_secondary_type(
            name=release_group_secondary_type.LIVE)

    def test__release_group_secondary_type__instance(self):
        self.assertIsInstance(self.subject, release_group_secondary_type)

    def test__release_group_secondary_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__release_group_secondary_type__name_choice(self):
        subject = release_group_secondary_type(name="Invalid Type")
        with self.assertRaises(ValidationError):
            subject.save()
