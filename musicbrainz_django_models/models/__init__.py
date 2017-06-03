from .area_type import area_type
from .area import area
from .gender import gender
from .instrument_type import instrument_type
from .instrument import instrument
from .artist_type import artist_type
from .artist import artist
from .artist_isni import artist_isni
from .artist_ipi import artist_ipi
from .artist_alias_type import artist_alias_type
from .artist_alias import artist_alias
from .work_type import work_type
from .language import language
from .work import work
from .artist_credit import artist_credit
from .release_group_primary_type import release_group_primary_type
from .release_group_secondary_type import release_group_secondary_type
from .release_group import release_group
from .release_status import release_status
from .release_packaging import release_packaging
from .script import script
from .release import release
from .recording import recording
from .label_type import label_type
from .label import label
from .alternative_release_type import alternative_release_type
from .alternative_release import alternative_release
from .medium_format import medium_format
from .medium import medium
from .alternative_medium import alternative_medium
from .alternative_track import alternative_track
from .track import track
from .alternative_medium_track import alternative_medium_track
from .editor import editor
from .annotation import annotation
from .application import application
from .tag import tag
from .area_tag import area_tag
from .area_gid_redirect import area_gid_redirect
from .area_alias_type import area_alias_type
from .area_alias import area_alias
from .area_annotation import area_annotation
from .area_tag_raw import area_tag_raw
from .artist_annotation import artist_annotation
from .artist_meta import artist_meta
from .artist_tag import artist_tag
from .artist_rating_raw import artist_rating_raw
from .artist_tag_raw import artist_tag_raw
from .artist_credit_name import artist_credit_name
from .artist_gid_redirect import artist_gid_redirect
from .autoeditor_election import autoeditor_election
from .autoeditor_election_vote import autoeditor_election_vote
from .cdtoc import cdtoc
from .release_raw import release_raw
from .cdtoc_raw import cdtoc_raw
from .country_area import country_area
from .deleted_entity import deleted_entity
from .edit import edit
from .edit_data import edit_data
from .edit_note import edit_note
from .edit_note_recipient import edit_note_recipient
from .edit_area import edit_area
from .edit_artist import edit_artist
from .event_type import event_type
from .edit_event import edit_event
from .event import event
from .edit_instrument import edit_instrument
from .edit_label import edit_label
from .edit_place import edit_place
from .place_type import place_type
from .place import place

# __all__ silences PEP8 `module imported but unused`:
__all__ = [
    area_type,
    area,
    gender,
    instrument_type,
    instrument,
    artist_type,
    artist,
    artist_isni,
    artist_ipi,
    artist_alias_type,
    artist_alias,
    work_type,
    language,
    work,
    artist_credit,
    release_group_primary_type,
    release_group_secondary_type,
    release_group,
    release_status,
    release_packaging,
    script,
    release,
    recording,
    label_type,
    label,
    alternative_release_type,
    alternative_release,
    medium_format,
    medium,
    alternative_medium,
    alternative_track,
    track,
    alternative_medium_track,
    editor,
    annotation,
    application,
    tag,
    area_tag,
    area_gid_redirect,
    area_alias_type,
    area_alias,
    area_annotation,
    area_tag_raw,
    artist_annotation,
    artist_meta,
    artist_tag,
    artist_rating_raw,
    artist_tag_raw,
    artist_credit_name,
    artist_gid_redirect,
    autoeditor_election,
    autoeditor_election_vote,
    cdtoc,
    release_raw,
    cdtoc_raw,
    country_area,
    deleted_entity,
    edit,
    edit_data,
    edit_note,
    edit_note_recipient,
    edit_area,
    edit_artist,
    event_type,
    edit_event,
    event,
    edit_instrument,
    edit_label,
    edit_place,
    place_type,
    place,
]
