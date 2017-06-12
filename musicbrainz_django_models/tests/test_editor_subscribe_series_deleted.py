from django.test import TestCase
from ..models import editor_subscribe_series_deleted


class test_editor_subscribe_series_deleted(TestCase):
    def setUp(self):
        self.subject = editor_subscribe_series_deleted()

    def test__editor_subscribe_series_deleted__instance(self):
        self.assertIsInstance(self.subject, editor_subscribe_series_deleted)

    def test__editor_subscribe_series_deleted__str(self):
        self.assertEqual(str(self.subject), 'Editor Subscribe Series Deleted')
