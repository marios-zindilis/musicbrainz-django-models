from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import track
from ..models import artist_credit
from ..models import medium
from ..models import medium_format
from ..models import release
from ..models import release_group
from ..models import release_group_primary_type
from ..models import recording


class test_track(TestCase):
    def setUp(self):
        # Artist Credit:
        self.ARTIST_CREDIT_NAME = 'Artist Credit'
        self.subject_artist_credit = artist_credit(name=self.ARTIST_CREDIT_NAME)
        # Medium:
        self.MEDIUM_NAME = 'Medium'
        self.MEDIUM_POSITION = 1
        self.subject_medium = medium(name=self.MEDIUM_NAME)
        # Medium Format:
        self.MEDIUM_FORMAT_NAME = 'Medium Format Name'
        self.subject_medium_format = medium_format(name=self.MEDIUM_FORMAT_NAME)
        # Release:
        self.RELEASE_NAME = 'Release Name'
        self.subject_release = release(name=self.RELEASE_NAME)
        # Release Group:
        self.SUBJECT_RELEASE_GROUP_NAME = 'Release Group Name'
        self.subject_release_group = release_group(name=self.SUBJECT_RELEASE_GROUP_NAME)
        # Release Group Primary Type:
        self.SUBJECT_RELEASE_GROUP_PRIMARY_TYPE_NAME = release_group_primary_type.ALBUM
        self.subject_release_group_primary_type = release_group_primary_type(
            name=self.SUBJECT_RELEASE_GROUP_PRIMARY_TYPE_NAME)
        # Recording:
        self.SUBJECT_RECORDING_NAME = 'Recording'
        self.subject_recording = recording(name=self.SUBJECT_RECORDING_NAME)
        # Track:
        self.subject = track(name='Name')

    def test__track__instance(self):
        self.assertIsInstance(self.subject, track)

    def test__track__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__track__length(self):
        # Artist Credit:
        self.subject_artist_credit.save()
        self.subject.artist_credit = self.subject_artist_credit
        # Medium Format:
        self.subject_medium_format.save()
        # Release Group Primary Type:
        self.subject_release_group_primary_type.save()
        # Release Group:
        self.subject_release_group.artist_credit = self.subject_artist_credit
        self.subject_release_group.type = self.subject_release_group_primary_type
        self.subject_release_group.save()
        # Release:
        self.subject_release.artist_credit = self.subject_artist_credit
        self.subject_release.release_group = self.subject_release_group
        self.subject_release.save()
        # Medium:
        self.subject_medium.release = self.subject_release
        self.subject_medium.format = self.subject_medium_format
        self.subject_medium.position = self.MEDIUM_POSITION
        self.subject_medium.save()
        self.subject.medium = self.subject_medium
        # Recording:
        self.subject_recording.artist_credit = self.subject_artist_credit
        self.subject_recording.save()
        self.subject.recording = self.subject_recording
        # Track:
        self.subject.position = 1
        self.subject.length = 0
        with self.assertRaises(ValidationError):
            self.subject.save()
