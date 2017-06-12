from django.test import TestCase
from ..models import editor_subscribe_series


class test_editor_subscribe_series(TestCase):
    def setUp(self):
        self.subject = editor_subscribe_series()

    def test__editor_subscribe_series__instance(self):
        self.assertIsInstance(self.subject, editor_subscribe_series)

    def test__editor_subscribe_series__str(self):
        self.assertEqual(str(self.subject), 'Editor Subscribe Series')
