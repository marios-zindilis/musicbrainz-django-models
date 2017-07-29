from django.test import TestCase
from ..models import l_label_recording


class test_l_label_recording(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_recording()

    def test__l_label_recording__instance(self):
        self.assertIsInstance(self.subject, l_label_recording)

    def test__l_label_recording__str(self):
        self.assertEqual(str(self.subject), 'L Label Recording')
