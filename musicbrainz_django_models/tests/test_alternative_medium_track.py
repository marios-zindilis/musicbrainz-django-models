from django.test import TestCase
from ..models import alternative_medium_track
from ..models import alternative_medium
from ..models import track


class test_alternative_medium_track(TestCase):
    def setUp(self):
        self.ALTERNATIVE_MEDIUM_NAME = 'Alternative Medium'
        self.TRACK_NAME = 'Track'
        self.subject_alternative_medium = alternative_medium(name=self.ALTERNATIVE_MEDIUM_NAME)
        self.subject_track = track(name=self.TRACK_NAME)
        self.subject = alternative_medium_track()

    def test__alternative_medium_track__instance(self):
        self.assertIsInstance(self.subject, alternative_medium_track)

    def test__alternative_medium_track__str(self):
        self.subject.alternative_medium = self.subject_alternative_medium
        self.subject.track = self.subject_track
        self.assertEqual(
            str(self.subject),
            '{} {}'.format(
                self.ALTERNATIVE_MEDIUM_NAME,
                self.TRACK_NAME))
