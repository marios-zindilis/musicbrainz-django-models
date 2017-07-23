from django.test import TestCase
from ..models import event_gid_redirect


class test_event_gid_redirect(TestCase):
    def setUp(self):
        self.subject = event_gid_redirect()

    def test__event_gid_redirect__instance(self):
        self.assertIsInstance(self.subject, event_gid_redirect)

    def test__event_gid_redirect__str(self):
        self.assertEqual(str(self.subject), 'Event GID Redirect')
