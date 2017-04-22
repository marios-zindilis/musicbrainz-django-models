from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_alias_type


class test_artist_alias_type(TestCase):
    def test_artist_alias_type_str(self):
        subject = artist_alias_type(name=artist_alias_type.ARTIST_NAME)
        self.assertEqual(str(subject), subject.name)

    def test_artist_alias_type_unicode(self):
        subject = artist_alias_type(name=artist_alias_type.LEGAL_NAME)
        self.assertEqual(subject.__unicode__(), subject.name)

    def test_artist_alias_type_name(self):
        subject = artist_alias_type(name='Invalid Type Name')
        with self.assertRaises(ValidationError):
            subject.save()
