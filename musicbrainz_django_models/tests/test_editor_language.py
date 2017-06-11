from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import editor_language


class test_editor_language(TestCase):
    def setUp(self):
        self.subject = editor_language()

    def test__editor_language__instance(self):
        self.assertIsInstance(self.subject, editor_language)

    def test__editor_language__str(self):
        self.assertEqual(str(self.subject), 'Editor Language')

    def test__editor_language__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
