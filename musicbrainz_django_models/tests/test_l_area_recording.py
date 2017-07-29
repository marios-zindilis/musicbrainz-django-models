from django.test import TestCase
from ..models import l_area_recording


class test_l_area_recording(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_recording()

    def test__l_area_recording__instance(self):
        self.assertIsInstance(self.subject, l_area_recording)

    def test__l_area_recording__str(self):
        self.assertEqual(str(self.subject), 'L Area Recording')
