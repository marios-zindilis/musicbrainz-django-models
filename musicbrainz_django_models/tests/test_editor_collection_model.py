from django.test import TestCase
from ..models import editor_collection_area
from ..models import editor_collection_artist
from ..models import editor_collection_event
from ..models import editor_collection_instrument
from ..models import editor_collection_label
from ..models import editor_collection_place
from ..models import editor_collection_recording
from ..models import editor_collection_release
from ..models import editor_collection_release_group
from ..models import editor_collection_series
from ..models import editor_collection_work


class test_editor_collection_area(TestCase):
    def setUp(self):
        self.MODELS = (
            editor_collection_area,
            editor_collection_artist,
            editor_collection_event,
            editor_collection_instrument,
            editor_collection_label,
            editor_collection_place,
            editor_collection_recording,
            editor_collection_release,
            editor_collection_release_group,
            editor_collection_series,
            editor_collection_work)

    def test__editor_collection_model(self):
        for model in self.MODELS:
            self.subject = model()
            self.assertIsInstance(self.subject, model)

            expected_str = ' '.join([_.title() for _ in model.__name__.split('_')])
            self.assertEqual(str(self.subject), expected_str)
