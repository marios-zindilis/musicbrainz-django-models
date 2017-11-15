from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import area_attribute
from ..models import artist_attribute
from ..models import event_attribute
from ..models import instrument_attribute
from ..models import label_attribute
from ..models import medium_attribute
from ..models import place_attribute
from ..models import recording_attribute
from ..models import release_attribute
from ..models import release_group_attribute
from ..models import series_attribute
from ..models import work_attribute


class test_model_attribute(TestCase):
    def setUp(self):
        self.MODELS = (
            area_attribute,
            artist_attribute,
            event_attribute,
            instrument_attribute,
            label_attribute,
            medium_attribute,
            place_attribute,
            recording_attribute,
            release_attribute,
            release_group_attribute,
            series_attribute,
            work_attribute,)

    def test__model_attribute(self):
        for model in self.MODELS:
            self.subject = model()
            self.assertIsInstance(self.subject, model)

            expected_str = ' '.join([_.title() for _ in model.__name__.split('_')])
            self.assertEqual(str(self.subject), expected_str)

            with self.assertRaises(ValidationError):
                self.subject.save()
