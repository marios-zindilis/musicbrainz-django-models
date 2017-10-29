from django.test import TestCase
from ..models import editor_watch_artist
from ..models import artist
from ..models import editor


class test_editor_watch_artist(TestCase):
    def setUp(self):
        self.subject_editor_name = 'Subject Editor Name'
        self.subject_artist_name = 'Subject Artist Name'

        self.subject_editor = editor(name=self.subject_editor_name)
        self.subject_artist = artist(name=self.subject_artist_name)

        self.subject = editor_watch_artist(
            editor=self.subject_editor, artist=self.subject_artist)

    def test__editor_watch_artist__instance(self):
        self.assertIsInstance(self.subject, editor_watch_artist)

    def test__editor_watch_artist__str(self):
        self.assertEqual(
            str(self.subject),
            'Subject Editor Name watches Subject Artist Name')
