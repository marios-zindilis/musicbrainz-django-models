from django.test import TestCase
from ..models import replication_control


class test_replication_control(TestCase):
    def setUp(self):
        self.subject = replication_control()

    def test__replication_control__instance(self):
        self.assertIsInstance(self.subject, replication_control)

    def test__replication_control__str(self):
        self.assertEqual(str(self.subject), 'Replication Control')
