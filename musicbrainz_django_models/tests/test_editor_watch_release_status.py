from django.test import TestCase
from ..models import editor_watch_release_status
from ..models import editor
from ..models import release_status


class test_editor_watch_release_status(TestCase):
    def setUp(self):
        self.subject_editor_name = 'Subject Editor Name'
        self.subject_release_status_name = 'Subject Release Status Name'

        self.subject_editor = editor(name=self.subject_editor_name)
        self.subject_release_status = release_status(name=self.subject_release_status_name)

        self.subject = editor_watch_release_status(
            editor=self.subject_editor,
            release_status=self.subject_release_status)

    def test__editor_watch_release_status__instance(self):
        self.assertIsInstance(self.subject, editor_watch_release_status)

    def test__editor_watch_release_status__str(self):
        self.assertEqual(
            str(self.subject),
            'Subject Editor Name watches Subject Release Status Name')
