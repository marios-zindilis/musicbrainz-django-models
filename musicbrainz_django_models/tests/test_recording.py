from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import recording, artist_credit


class test_recording(TestCase):
    def setUp(self):
        self.subject = recording(name='Name')

    def test__recording__instance(self):
        self.assertIsInstance(self.subject, recording)

    def test__recording__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__recording__length(self):
        subject_artist_credit = artist_credit(name='Something')
        subject_artist_credit.save()
        self.subject.length = 0
        self.subject.artist_credit = subject_artist_credit
        with self.assertRaises(ValidationError):
            self.subject.save()
