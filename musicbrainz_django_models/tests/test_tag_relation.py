from django.test import TestCase
from ..models import tag_relation


class test_tag_relation(TestCase):
    def setUp(self):
        self.subject = tag_relation()

    def test__tag_relation__instance(self):
        self.assertIsInstance(self.subject, tag_relation)

    def test__tag_relation__str(self):
        self.assertEqual(str(self.subject), 'Tag Relation')
