from django.test import TestCase
from ..models import editor_subscribe_artist


class test_editor_subscribe_artist(TestCase):
    def setUp(self):
        self.subject = editor_subscribe_artist()

    def test__editor_subscribe_artist__instance(self):
        self.assertIsInstance(self.subject, editor_subscribe_artist)

    def test__editor_subscribe_artist__str(self):
        self.assertEqual(str(self.subject), 'Editor Subscribe Artist')
