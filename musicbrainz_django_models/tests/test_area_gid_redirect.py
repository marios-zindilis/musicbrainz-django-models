from django.test import TestCase
from ..models import area_gid_redirect


class test_area_gid_redirect(TestCase):
    def setUp(self):
        self.subject = area_gid_redirect()

    def test__area_gid_redirect__instance(self):
        self.assertIsInstance(self.subject, area_gid_redirect)

    def test__area_gid_redirect__str(self):
        self.assertEqual(str(self.subject), str(self.subject.gid))
