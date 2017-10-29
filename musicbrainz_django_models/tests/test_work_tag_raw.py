from django.test import TestCase
from ..models import work_tag_raw


class test_work_tag_raw(TestCase):
    def setUp(self):
        self.subject = work_tag_raw()

    def test__work_tag_raw__instance(self):
        self.assertIsInstance(self.subject, work_tag_raw)

    def test__work_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Work Tag Raw')
