from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import gender


class test_gender(TestCase):
    def test__gender__str(self):
        subject = gender(name='Female')
        self.assertEqual(str(subject), subject.name)

    def test__gender__unicode(self):
        subject = gender(name='Male')
        self.assertEqual(subject.__unicode__(), subject.name)

    def test__gender__name_choice(self):
        subject = gender(name='Invalid')
        with self.assertRaises(ValidationError):
            subject.save()
