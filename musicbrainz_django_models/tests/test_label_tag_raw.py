from django.test import TestCase
from ..models import label_tag_raw


class test_label_tag_raw(TestCase):
    def setUp(self):
        self.subject = label_tag_raw()

    def test__label_tag_raw__instance(self):
        self.assertIsInstance(self.subject, label_tag_raw)

    def test__label_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Label Tag Raw')
