from django.test import TestCase
from django.core.exceptions import ValidationError
import string
import random
from ..models import area_alias_type
from ..models import artist_alias_type
from ..models import event_alias_type
from ..models import instrument_alias_type
from ..models import label_alias_type
from ..models import place_alias_type
from ..models import recording_alias_type
from ..models import release_alias_type
from ..models import release_group_alias_type
from ..models import series_alias_type
from ..models import work_alias_type


class test_model_alias_type(TestCase):
    def setUp(self):
        self.MODELS = (
            area_alias_type,
            artist_alias_type,
            event_alias_type,
            instrument_alias_type,
            label_alias_type,
            place_alias_type,
            recording_alias_type,
            release_alias_type,
            release_group_alias_type,
            series_alias_type,
            work_alias_type)

        # A random string to be used as the name:
        self.subject_name = ''.join(random.choice(string.printable) for _ in range(16))

    def test__model_alias_type(self):
        for model in self.MODELS:
            self.subject = model(name=self.subject_name)
            self.assertIsInstance(self.subject, model)
            self.assertEquals(str(self.subject), self.subject.name)

            if hasattr(self.subject, 'NAME_CHOICES_LIST'):
                with self.assertRaises(ValidationError):
                    self.subject.save()
