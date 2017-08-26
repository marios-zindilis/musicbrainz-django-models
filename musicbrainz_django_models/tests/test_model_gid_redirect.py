from django.test import TestCase
from ..models import area_gid_redirect
from ..models import artist_gid_redirect
from ..models import event_gid_redirect
from ..models import instrument_gid_redirect
from ..models import label_gid_redirect
from ..models import place_gid_redirect
from ..models import recording_gid_redirect
from ..models import release_gid_redirect
from ..models import release_group_gid_redirect
from ..models import series_gid_redirect
from ..models import track_gid_redirect
from ..models import url_gid_redirect
from ..models import work_gid_redirect


class test_model_gid_redirect(TestCase):
    def setUp(self):
        self.MODELS = (
            area_gid_redirect,
            artist_gid_redirect,
            event_gid_redirect,
            instrument_gid_redirect,
            label_gid_redirect,
            place_gid_redirect,
            recording_gid_redirect,
            release_gid_redirect,
            release_group_gid_redirect,
            series_gid_redirect,
            track_gid_redirect,
            url_gid_redirect,
            work_gid_redirect)

    def test__model_gid_redirect(self):
        for model in self.MODELS:
            # If the model is `release_group_gid_redirect`, the expected string
            # is "Release Group GID Redirect":
            expected_str = '{} GID Redirect'.format(  # model.__name__.split('_')[:-2].title())
                ' '.join([_.title() for _ in model.__name__.split('_')[:-2]]))
            self.subject = model()
            self.assertIsInstance(self.subject, model)
            self.assertEqual(str(self.subject), expected_str)
