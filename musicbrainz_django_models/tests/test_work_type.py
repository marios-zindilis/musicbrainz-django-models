from django.test import TestCase
from ..models import work_type


class test_work_type(TestCase):
    def test__work_type__str(self):
        subject = work_type(name='Song')
        self.assertEqual(str(subject), subject.name)
