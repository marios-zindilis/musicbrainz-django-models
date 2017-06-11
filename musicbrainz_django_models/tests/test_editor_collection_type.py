from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import editor_collection_type


class test_editor_collection_type(TestCase):
    def setUp(self):
        self.subject = editor_collection_type(name='Name')

    def test__editor_collection_type__instance(self):
        self.assertIsInstance(self.subject, editor_collection_type)

    def test__editor_collection_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__editor_collection_type__name_choice(self):
        with self.assertRaises(ValidationError):
            self.subject.save()
