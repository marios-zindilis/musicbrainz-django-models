from django.test import TestCase
from ..models import l_label_release_group


class test_l_label_release_group(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_release_group()

    def test__l_label_release_group__instance(self):
        self.assertIsInstance(self.subject, l_label_release_group)

    def test__l_label_release_group__str(self):
        self.assertEqual(str(self.subject), 'L Label Release Group')
