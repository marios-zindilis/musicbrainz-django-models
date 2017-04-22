from django.test import TestCase
from ..models import artist, artist_alias, artist_alias_type


class test_artist_alias(TestCase):
    def test__artist_alias__str(self):
        subject = artist_alias(name='Bob Squarepants')
        self.assertEqual(str(subject), subject.name)

    def test__artist_alias__unicode(self):
        subject = artist_alias(name='Jibbers Crabst')
        self.assertEqual(subject.__unicode__(), subject.name)

    def test__artist_alias__end_date_year(self):
        """
        When the `end_date_year` of an `artist_alias` is not None, `ended`
        must be True.
        """

        subject_artist = artist(name='Elvis Presley')
        subject_artist.save()

        subject_artist_alias_type = artist_alias_type(
            name=artist_alias_type.ARTIST_NAME)
        subject_artist_alias_type.save()

        subject = artist_alias(
            name='The King',
            artist=subject_artist,
            type=subject_artist_alias_type,
            end_date_year=1977)
        subject.save()

        self.assertTrue(subject.ended)

    def test__artist_alias__end_date_month(self):
        """
        When the `end_date_month` of an `artist_alias` is not None, `ended`
        must be True.
        """

        subject_artist = artist(name='Elvis Presley')
        subject_artist.save()

        subject_artist_alias_type = artist_alias_type(
            name=artist_alias_type.SEARCH_HINT)
        subject_artist_alias_type.save()

        subject = artist_alias(
            name='The King',
            artist=subject_artist,
            type=subject_artist_alias_type,
            end_date_month=8)
        subject.save()

        self.assertTrue(subject.ended)

    def test__artist_alias__end_date_day(self):
        """
        When the `end_date_day` of an `artist_alias` is not None, `ended` must
        be True.
        """

        subject_artist = artist(name='Elvis Presley')
        subject_artist.save()

        subject_artist_alias_type = artist_alias_type(
            name=artist_alias_type.ARTIST_NAME)
        subject_artist_alias_type.save()

        subject = artist_alias(
            name='The King',
            artist=subject_artist,
            type=subject_artist_alias_type,
            end_date_day=16)
        subject.save()

        self.assertTrue(subject.ended)

    def test__artist_alias__primary_for_locale(self):
        """
        When the `locale` of an `artist_alias` is empty, `primary_for_locale`
        must be False.
        """
        subject_artist = artist(name='Elvis Presley')
        subject_artist.save()

        subject_artist_alias_type = artist_alias_type(
            name=artist_alias_type.SEARCH_HINT)
        subject_artist_alias_type.save()

        subject = artist_alias(
            artist=subject_artist,
            type=subject_artist_alias_type,
            locale=None,
            primary_for_locale=True)
        subject.save()

        self.assertFalse(subject.primary_for_locale)

    def test__artist_alias__search_hint(self):
        """
        When the `type` of an `artist_alias` is "Search hint", then the
        `sort_name` must be equal to the `name`, `primary_for_locale` must be
        False, `locale` must be empty, and all `*_date_*` fields must be
        empty.
        """

        subject_artist = artist(name='Elvis Presley')
        subject_artist.save()

        subject_artist_alias_type = artist_alias_type(
            name=artist_alias_type.SEARCH_HINT)
        subject_artist_alias_type.save()

        subject = artist_alias(
            name='The King',
            sort_name = 'Not The King',
            artist=subject_artist,
            type=subject_artist_alias_type,
            end_date_year=1977,
            end_date_month=8,
            end_date_day=16,
            begin_date_year=1935,
            begin_date_month=1,
            begin_date_day=8,
            locale='US',
            primary_for_locale=True)
        subject.save()

        self.assertEqual(subject.sort_name, subject.name)
        self.assertIsNone(subject.end_date_year)
        self.assertIsNone(subject.end_date_month)
        self.assertIsNone(subject.end_date_day)
        self.assertIsNone(subject.begin_date_year)
        self.assertIsNone(subject.begin_date_month)
        self.assertIsNone(subject.begin_date_day)
        self.assertIsNone(subject.locale)
        self.assertFalse(subject.primary_for_locale)
