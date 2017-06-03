from django.test import TestCase
from ..models import edit_label
from ..models import edit
from ..models import editor
from ..models import language
from ..models import label
import datetime


class test_edit_label(TestCase):
    def setUp(self):
        self.subject = edit_label()
        # set up the `label` related to `edit_label`:
        self.subject_label = label(name='Name')
        self.subject_label.save()
        # set up the `language` related to `edit`:
        self.subject_language = language(name='Language', iso_code_3='ISO')
        self.subject_language.save()
        # set up the `editor` related to `edit`:
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

    def test__edit_label__instance(self):
        self.assertIsInstance(self.subject, edit_label)

    def test__edit_label__str(self):
        self.assertEqual(str(self.subject), 'Edit Label')

    def test__edit_label__status(self):
        self.subject.edit = self.subject_edit
        self.subject.label = self.subject_label
        self.subject.save()
        self.assertEqual(self.subject.status, self.SUBJECT_EDIT_STATUS)
