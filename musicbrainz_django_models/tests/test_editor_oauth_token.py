from django.test import TestCase
from ..models import editor_oauth_token


class test_editor_oauth_token(TestCase):
    def setUp(self):
        self.subject = editor_oauth_token()

    def test__editor_oauth_token__instance(self):
        self.assertIsInstance(self.subject, editor_oauth_token)

    def test__editor_oauth_token__str(self):
        self.assertEqual(str(self.subject), 'Editor OAuth Token')
