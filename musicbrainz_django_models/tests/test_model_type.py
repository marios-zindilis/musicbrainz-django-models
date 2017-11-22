"""
Tests for models that subclass `abstract.model_type`, namely:

1.  :class:`area_alias_type`
2.  :class:`artist_alias_type`
3.  :class:`event_alias_type`
4.  :class:`instrument_alias_type`
5.  :class:`label_alias_type`
6.  :class:`place_alias_type`
7.  :class:`recording_alias_type`
8.  :class:`release_alias_type`
9.  :class:`release_group_alias_type`
10. :class:`series_alias_type`
11. :class:`work_alias_type`
12. :class:`area_type`
13. :class:`artist_type`
14. :class:`event_type`
15. :class:`instrument_type`
16. :class:`label_type`
17. :class:`place_type`
18. :class:`series_type`
19. :class:`work_type`
20. :class:`release_group_primary_type`
21. :class:`release_group_secondary_type`
22. :class:`alternative_release_type`
23. :class:`series_ordering_type`
"""

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
from ..models import area_type
from ..models import artist_type
from ..models import event_type
from ..models import instrument_type
from ..models import label_type
from ..models import place_type
from ..models import series_type
from ..models import work_type
from ..models import release_group_primary_type
from ..models import release_group_secondary_type
from ..models import alternative_release_type
from ..models import series_ordering_type


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
            work_alias_type,
            area_type,
            artist_type,
            event_type,
            instrument_type,
            label_type,
            place_type,
            series_type,
            work_type,
            release_group_primary_type,
            release_group_secondary_type,
            alternative_release_type,
            series_ordering_type)

        # A random string to be used as the name:
        self.subject_name = ''.join(random.choice(string.printable) for _ in range(16))

    def test__model_alias_type(self):
        for model in self.MODELS:
            self.subject = model(name=self.subject_name)
            self.assertIsInstance(self.subject, model)
            self.assertEquals(str(self.subject), self.subject_name)

            if hasattr(self.subject, 'NAME_CHOICES_LIST'):
                with self.assertRaises(ValidationError):
                    self.subject.save()
