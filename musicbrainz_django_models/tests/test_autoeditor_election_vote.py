from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import autoeditor_election_vote


class test_autoeditor_election_vote(TestCase):
    def setUp(self):
        self.subject = autoeditor_election_vote()

    def test__autoeditor_election_vote__instance(self):
        self.assertIsInstance(self.subject, autoeditor_election_vote)

    def test__autoeditor_election_vote__str(self):
        self.assertEqual(str(self.subject), 'Autoeditor Election Vote')

    def test__autoeditor_election_vote__vote_min_value(self):
        self.subject.vote = autoeditor_election_vote.VOTE_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__autoeditor_election_vote__vote_max_value(self):
        self.subject.vote = autoeditor_election_vote.VOTE_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
