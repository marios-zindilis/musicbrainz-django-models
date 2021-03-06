from django.test import TestCase
from ..models import release_group_alias
from ..models import release_group
from ..models import release_group_alias_type
from ..models import artist_credit


class test_release_group_alias(TestCase):
    def setUp(self):
        self.subject_artist_credit = artist_credit(name='Artist Credit')
        self.subject_artist_credit.save()

        self.subject_release_group = release_group(name='Release Group', artist_credit=self.subject_artist_credit)
        self.subject_release_group.save()

        self.subject_release_group_alias_type = release_group_alias_type(name='Release Group Alias Type')
        self.subject_release_group_alias_type.save()

        self.subject = release_group_alias(name='Name', type=self.subject_release_group_alias_type)

    def test__release_group_alias__instance(self):
        self.assertIsInstance(self.subject, release_group_alias)

    def test__release_group_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__release_group_alias__ended(self):
        self.subject.release_group = self.subject_release_group
        self.subject.save()
        self.assertFalse(self.subject.ended)

    def test__release_group_alias__end_date_year(self):
        self.subject.release_group = self.subject_release_group
        self.subject.end_date_year = 1212
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__release_group_alias__end_date_month(self):
        self.subject.release_group = self.subject_release_group
        self.subject.end_date_month = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__release_group_alias__end_date_day(self):
        self.subject.release_group = self.subject_release_group
        self.subject.end_date_day = 12
        self.subject.save()
        self.assertTrue(self.subject.ended)

    def test__release_group_alias__locale_is_none(self):
        self.subject.release_group = self.subject_release_group
        self.subject.locale = None
        self.subject.save()
        self.assertFalse(self.subject.primary_for_locale)
