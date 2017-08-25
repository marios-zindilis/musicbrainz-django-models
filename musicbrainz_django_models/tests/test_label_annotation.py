from django.test import TestCase
from ..models import label_annotation


class test_label_annotation(TestCase):
    def setUp(self):
        self.subject = label_annotation()

    def test__label_annotation__instance(self):
        self.assertIsInstance(self.subject, label_annotation)

    def test__label_annotation__str(self):
        self.assertEqual(str(self.subject), 'Label Annotation')
