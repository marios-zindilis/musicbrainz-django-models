from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import alternative_track
from ..models import artist_credit


class test_alternative_track(TestCase):
    def setUp(self):
        self.ARTIST_CREDIT_NAME = 'Artist Credit'
        self.subject = alternative_track(name='Name')
        self.subject_artist_credit = artist_credit(name=self.ARTIST_CREDIT_NAME)

    def test__alternative_track__instance(self):
        self.assertIsInstance(self.subject, alternative_track)

    # If there is a name, str will return it:
    def test__alternative_track__str_name(self):
        self.assertEqual(str(self.subject), self.subject.name)

    # If there is an artist_credit but no name, str will return it:
    def test__alternative_track__str_artist_credit(self):
        self.subject.name = None
        self.subject.artist_credit = self.subject_artist_credit
        self.assertEqual(str(self.subject), self.ARTIST_CREDIT_NAME)

    # If there are both name and artist_credit, str should return the name:
    def test__alternative_tracl__str_both(self):
        self.subject.artist_credit = self.subject_artist_credit
        self.assertEqual(str(self.subject), self.subject.name)

    def test__alternative_track__name_or_artist_credit(self):
        self.subject.name = None
        with self.assertRaises(ValidationError):
            self.subject.save()
