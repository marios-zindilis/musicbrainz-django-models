"""
Tests for models that subclass `abstract__model_meta`.
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import artist_meta
from ..models import event_meta
from ..models import label_meta
from ..models import recording_meta
from ..models import work_meta


class test_model_meta_mixin(object):
    def test__model_meta__rating_min_value(self):
        self.subject.rating = self.subject.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__model_meta__rating_max_value(self):
        self.subject.rating = self.subject.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()


class test_artist_meta(TestCase, test_model_meta_mixin):
    """
    Tests for the `artist_meta` model.
    """
    def setUp(self):
        self.subject = artist_meta()

    def test__artist_meta__instance(self):
        self.assertIsInstance(self.subject, artist_meta)

    def test__artist_meta__str(self):
        self.assertEqual(str(self.subject), 'Artist Meta')


class test_event_meta(TestCase, test_model_meta_mixin):
    """
    Tests for the `event_meta` model.
    """
    def setUp(self):
        self.subject = event_meta()

    def test__event_meta__instance(self):
        self.assertIsInstance(self.subject, event_meta)

    def test__event_meta__str(self):
        self.assertEqual(str(self.subject), 'Event Meta')


class test_label_meta(TestCase, test_model_meta_mixin):
    """
    Tests for the `label_meta` model.
    """
    def setUp(self):
        self.subject = label_meta()

    def test__label_meta__instance(self):
        self.assertIsInstance(self.subject, label_meta)

    def test__label_meta__str(self):
        self.assertEqual(str(self.subject), 'Label Meta')


class test_recording_meta(TestCase, test_model_meta_mixin):
    """
    Tests for the `recording_meta` model.
    """
    def setUp(self):
        self.subject = recording_meta()

    def test__recording_meta__instance(self):
        self.assertIsInstance(self.subject, recording_meta)

    def test__recording_meta__str(self):
        self.assertEqual(str(self.subject), 'Recording Meta')


class test_work_meta(TestCase, test_model_meta_mixin):
    """
    Tests for the `work_meta` model.
    """
    def setUp(self):
        self.subject = work_meta()

    def test__work_meta__instance(self):
        self.assertIsInstance(self.subject, work_meta)

    def test__work_meta__str(self):
        self.assertEqual(str(self.subject), 'Work Meta')
