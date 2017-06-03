from django.test import TestCase
from ..models import edit_artist
from ..models import edit
from ..models import editor
from ..models import language
from ..models import artist
import datetime


class test_edit_artist(TestCase):
    def setUp(self):
        self.subject = edit_artist()
        # set up the `artist` related to `edit_artist`:
        self.subject_artist = artist(name='Name')
        self.subject_artist.save()
        # set up the `language` related to `edit_artist`:
        self.subject_language = language(name='Language', iso_code_3='ISO')
        self.subject_language.save()
        # set up the `editor` related to `edit_artist`:
        self.subject_editor = editor(name='Editor')
        self.subject_editor.save()
        # set up the related `edit`:
        self.SUBJECT_EDIT_TYPE = 1
        self.SUBJECT_EDIT_STATUS = 1
        self.SUBJECT_EDIT_EXPIRE_TIME = datetime.datetime.now()
        self.subject_edit = edit(
            status=self.SUBJECT_EDIT_STATUS,
            type=self.SUBJECT_EDIT_TYPE,
            expire_time=self.SUBJECT_EDIT_EXPIRE_TIME,
            editor=self.subject_editor,
            language=self.subject_language)
        self.subject_edit.save()

    def test__edit_artist__instance(self):
        self.assertIsInstance(self.subject, edit_artist)

    def test__edit_artist__str(self):
        self.assertEqual(str(self.subject), 'Edit Artist')

    def test__edit_artist__status(self):
        self.subject.edit = self.subject_edit
        self.subject.artist = self.subject_artist
        self.subject.save()
        self.assertEqual(self.subject.status, self.SUBJECT_EDIT_STATUS)
