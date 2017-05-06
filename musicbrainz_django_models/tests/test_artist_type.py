from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_type


class test_artist_type(TestCase):
    def test__artist_type__instance(self):
        subject = artist_type(name=artist_type.PERSON)
        self.assertIsInstance(subject, artist_type)

    def test__artist_type__str(self):
        subject = artist_type(name=artist_type.GROUP)
        self.assertEqual(str(subject), subject.name)

    def test__artict_type__name_choice(self):
        subject = artist_type(name="Invalid Type")
        with self.assertRaises(ValidationError):
            subject.save()
