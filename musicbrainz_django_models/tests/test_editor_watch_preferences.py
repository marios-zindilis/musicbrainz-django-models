from django.test import TestCase
from ..models import editor_watch_preferences
from ..models import editor


class test_editor_watch_preferences(TestCase):
    def setUp(self):
        self.subject_editor = editor(name='Subject Editor Name')
        self.subject = editor_watch_preferences(editor=self.subject_editor)

    def test__editor_watch_preferences__instance(self):
        self.assertIsInstance(self.subject, editor_watch_preferences)

    def test__editor_watch_preferences__str(self):
        self.assertEqual(str(self.subject), 'Editor Watch Preferences')
