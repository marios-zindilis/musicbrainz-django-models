from django.test import TestCase
from ..models import editor_watch_release_group_type
from ..models import editor
from ..models import release_group_primary_type


class test_editor_watch_release_group_type(TestCase):
    def setUp(self):
        self.subject_editor_name = 'Subject Editor Name'
        self.subject_release_group_type_name = 'Release Group Type Name'

        self.subject_editor = editor(name=self.subject_editor_name)
        self.subject_release_group_type = release_group_primary_type(name=self.subject_release_group_type_name)

        self.subject = editor_watch_release_group_type(
            editor=self.subject_editor,
            release_group_type=self.subject_release_group_type)

    def test__editor_watch_release_group_type__instance(self):
        self.assertIsInstance(self.subject, editor_watch_release_group_type)

    def test__editor_watch_release_group_type__str(self):
        self.assertEqual(
            str(self.subject),
            'Subject Editor Name watches Release Group Type Name')
