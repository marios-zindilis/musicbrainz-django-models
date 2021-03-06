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
from .edit_release import edit_release
from .edit_release_group import edit_release_group
from .edit_recording import edit_recording
from .edit_series import edit_series
from .series_type import series_type
from .link_attribute_type import link_attribute_type
from .link_text_attribute_type import link_text_attribute_type
from .series_ordering_type import series_ordering_type
from .series import series
from .edit_work import edit_work
from .url import url
from .edit_url import edit_url
from .editor_language import editor_language
from .editor_preference import editor_preference
from .editor_subscribe_artist import editor_subscribe_artist
from .editor_subscribe_artist_deleted import editor_subscribe_artist_deleted
from .editor_collection_type import editor_collection_type
from .editor_collection import editor_collection
from .editor_subscribe_collection import editor_subscribe_collection
from .editor_subscribe_label import editor_subscribe_label
from .editor_subscribe_label_deleted import editor_subscribe_label_deleted
from .editor_subscribe_editor import editor_subscribe_editor
from .editor_subscribe_series import editor_subscribe_series
from .editor_subscribe_series_deleted import editor_subscribe_series_deleted
from .event_meta import event_meta
from .event_rating_raw import event_rating_raw
from .event_tag_raw import event_tag_raw
from .event_alias_type import event_alias_type
from .event_alias import event_alias
from .event_annotation import event_annotation
from .event_gid_redirect import event_gid_redirect
from .event_tag import event_tag
from .instrument_gid_redirect import instrument_gid_redirect
from .instrument_alias_type import instrument_alias_type
from .instrument_alias import instrument_alias
from .instrument_annotation import instrument_annotation
from .link_type import link_type
from .instrument_tag import instrument_tag
from .instrument_tag_raw import instrument_tag_raw
from .iso_3166_1 import iso_3166_1
from .iso_3166_2 import iso_3166_2
from .iso_3166_3 import iso_3166_3
from .isrc import isrc
from .iswc import iswc
from .link import link
from .l_area_area import l_area_area
from .l_area_artist import l_area_artist
from .l_area_event import l_area_event
from .l_area_instrument import l_area_instrument
from .l_area_label import l_area_label
from .l_area_place import l_area_place
from .l_area_recording import l_area_recording
from .l_area_release import l_area_release
from .l_area_release_group import l_area_release_group
from .l_area_series import l_area_series
from .l_area_url import l_area_url
from .l_area_work import l_area_work
from .l_artist_artist import l_artist_artist
from .l_artist_event import l_artist_event
from .l_artist_instrument import l_artist_instrument
from .l_artist_label import l_artist_label
from .l_artist_place import l_artist_place
from .l_artist_recording import l_artist_recording
from .l_artist_release import l_artist_release
from .l_artist_release_group import l_artist_release_group
from .l_artist_series import l_artist_series
from .l_artist_url import l_artist_url
from .l_artist_work import l_artist_work
from .l_event_event import l_event_event
from .l_event_instrument import l_event_instrument
from .l_event_label import l_event_label
from .l_event_place import l_event_place
from .l_event_recording import l_event_recording
from .l_event_release import l_event_release
from .l_event_release_group import l_event_release_group
from .l_event_series import l_event_series
from .l_event_url import l_event_url
from .l_event_work import l_event_work
from .l_label_label import l_label_label
from .l_instrument_instrument import l_instrument_instrument
from .l_instrument_label import l_instrument_label
from .l_instrument_place import l_instrument_place
from .l_instrument_recording import l_instrument_recording
from .l_instrument_release import l_instrument_release
from .l_instrument_release_group import l_instrument_release_group
from .l_instrument_series import l_instrument_series
from .l_instrument_url import l_instrument_url
from .l_instrument_work import l_instrument_work
from .l_label_place import l_label_place
from .l_label_recording import l_label_recording
from .l_label_release import l_label_release
from .l_label_release_group import l_label_release_group
from .l_label_series import l_label_series
from .l_label_url import l_label_url
from .l_label_work import l_label_work
from .l_place_place import l_place_place
from .l_place_recording import l_place_recording
from .l_place_release import l_place_release
from .l_place_release_group import l_place_release_group
from .l_place_series import l_place_series
from .l_place_url import l_place_url
from .l_place_work import l_place_work
from .l_recording_recording import l_recording_recording
from .l_recording_release import l_recording_release
from .l_recording_release_group import l_recording_release_group
from .l_recording_series import l_recording_series
from .l_recording_url import l_recording_url
from .l_recording_work import l_recording_work
from .l_release_release import l_release_release
from .l_release_release_group import l_release_release_group
from .l_release_series import l_release_series
from .l_release_url import l_release_url
from .l_release_work import l_release_work
from .l_release_group_release_group import l_release_group_release_group
from .l_release_group_series import l_release_group_series
from .l_release_group_url import l_release_group_url
from .l_release_group_work import l_release_group_work
from .l_series_series import l_series_series
from .l_series_url import l_series_url
from .l_series_work import l_series_work
from .l_url_url import l_url_url
from .l_url_work import l_url_work
from .l_work_work import l_work_work
from .vote import vote
from .label_rating_raw import label_rating_raw
from .recording_rating_raw import recording_rating_raw
from .label_tag_raw import label_tag_raw
from .label_alias_type import label_alias_type
from .label_alias import label_alias
from .label_annotation import label_annotation
from .label_ipi import label_ipi
from .label_isni import label_isni
from .label_meta import label_meta
from .recording_meta import recording_meta
from .work_meta import work_meta
from .label_gid_redirect import label_gid_redirect
from .place_gid_redirect import place_gid_redirect
from .recording_gid_redirect import recording_gid_redirect
from .release_gid_redirect import release_gid_redirect
from .release_group_gid_redirect import release_group_gid_redirect
from .series_gid_redirect import series_gid_redirect
from .track_gid_redirect import track_gid_redirect
from .url_gid_redirect import url_gid_redirect
from .work_gid_redirect import work_gid_redirect
from .label_tag import label_tag
from .place_tag import place_tag
from .recording_tag import recording_tag
from .release_tag import release_tag
from .release_group_tag import release_group_tag
from .series_tag import series_tag
from .work_tag import work_tag
from .link_attribute import link_attribute
from .link_creditable_attribute_type import link_creditable_attribute_type
from .link_attribute_credit import link_attribute_credit
from .link_attribute_text_value import link_attribute_text_value
from .link_type_attribute_type import link_type_attribute_type
from .editor_collection_area import editor_collection_area
from .editor_collection_artist import editor_collection_artist
from .editor_collection_event import editor_collection_event
from .editor_collection_instrument import editor_collection_instrument
from .editor_collection_label import editor_collection_label
from .editor_collection_place import editor_collection_place
from .editor_collection_recording import editor_collection_recording
from .editor_collection_release import editor_collection_release
from .editor_collection_release_group import editor_collection_release_group
from .editor_collection_series import editor_collection_series
from .editor_collection_work import editor_collection_work
from .editor_collection_deleted_entity import editor_collection_deleted_entity
from .place_alias_type import place_alias_type
from .recording_alias_type import recording_alias_type
from .release_alias_type import release_alias_type
from .release_group_alias_type import release_group_alias_type
from .series_alias_type import series_alias_type
from .work_alias_type import work_alias_type
from .place_alias import place_alias
from .editor_oauth_token import editor_oauth_token
from .editor_watch_preferences import editor_watch_preferences
from .editor_watch_artist import editor_watch_artist
from .editor_watch_release_group_type import editor_watch_release_group_type
from .editor_watch_release_status import editor_watch_release_status
from .medium_cdtoc import medium_cdtoc
from .orderable_link_type import orderable_link_type
from .place_annotation import place_annotation
from .place_tag_raw import place_tag_raw
from .recording_tag_raw import recording_tag_raw
from .release_tag_raw import release_tag_raw
from .release_group_tag_raw import release_group_tag_raw
from .series_tag_raw import series_tag_raw
from .work_tag_raw import work_tag_raw
from .replication_control import replication_control
from .recording_alias import recording_alias
from .release_alias import release_alias
from .release_group_alias import release_group_alias
from .series_alias import series_alias
from .work_alias import work_alias
from .recording_annotation import recording_annotation
from .release_annotation import release_annotation
from .release_group_annotation import release_group_annotation
from .series_annotation import series_annotation
from .work_annotation import work_annotation
from .tag_relation import tag_relation
from .track_raw import track_raw
from .medium_index import medium_index
from .release_group_rating_raw import release_group_rating_raw
from .work_rating_raw import work_rating_raw
from .release_country import release_country
from .release_unknown_country import release_unknown_country
from .release_meta import release_meta
from .release_coverart import release_coverart
from .release_label import release_label
from .release_group_meta import release_group_meta
from .release_group_secondary_type_join import release_group_secondary_type_join
from .work_attribute_type import work_attribute_type
from .work_attribute_type_allowed_value import work_attribute_type_allowed_value
from .work_attribute import work_attribute
from .work_language import work_language
from .old_editor_name import old_editor_name
from .area_attribute_type import area_attribute_type
from .artist_attribute_type import artist_attribute_type
from .event_attribute_type import event_attribute_type
from .instrument_attribute_type import instrument_attribute_type
from .label_attribute_type import label_attribute_type
from .medium_attribute_type import medium_attribute_type
from .place_attribute_type import place_attribute_type
from .recording_attribute_type import recording_attribute_type
from .release_attribute_type import release_attribute_type
from .release_group_attribute_type import release_group_attribute_type
from .series_attribute_type import series_attribute_type
from .area_attribute_type_allowed_value import area_attribute_type_allowed_value
from .artist_attribute_type_allowed_value import artist_attribute_type_allowed_value
from .event_attribute_type_allowed_value import event_attribute_type_allowed_value
from .instrument_attribute_type_allowed_value import instrument_attribute_type_allowed_value
from .label_attribute_type_allowed_value import label_attribute_type_allowed_value
from .medium_attribute_type_allowed_value import medium_attribute_type_allowed_value
from .place_attribute_type_allowed_value import place_attribute_type_allowed_value
from .recording_attribute_type_allowed_value import recording_attribute_type_allowed_value
from .release_attribute_type_allowed_value import release_attribute_type_allowed_value
from .release_group_attribute_type_allowed_value import release_group_attribute_type_allowed_value
from .series_attribute_type_allowed_value import series_attribute_type_allowed_value
from .area_attribute import area_attribute
from .artist_attribute import artist_attribute
from .medium_attribute_type_allowed_format import medium_attribute_type_allowed_format
from .medium_attribute_type_allowed_value_allowed_format import medium_attribute_type_allowed_value_allowed_format
from .event_attribute import event_attribute
from .instrument_attribute import instrument_attribute
from .label_attribute import label_attribute
from .medium_attribute import medium_attribute
from .place_attribute import place_attribute
from .recording_attribute import recording_attribute
from .release_attribute import release_attribute
from .release_group_attribute import release_group_attribute
from .series_attribute import series_attribute

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
    edit_release,
    edit_release_group,
    edit_recording,
    edit_series,
    series_type,
    link_attribute_type,
    link_text_attribute_type,
    series_ordering_type,
    series,
    edit_work,
    url,
    edit_url,
    editor_language,
    editor_preference,
    editor_subscribe_artist,
    editor_subscribe_artist_deleted,
    editor_collection_type,
    editor_collection,
    editor_subscribe_collection,
    editor_subscribe_label,
    editor_subscribe_label_deleted,
    editor_subscribe_editor,
    editor_subscribe_series,
    editor_subscribe_series_deleted,
    event_meta,
    event_rating_raw,
    event_tag_raw,
    event_alias_type,
    event_alias,
    event_annotation,
    event_gid_redirect,
    event_tag,
    instrument_gid_redirect,
    instrument_alias_type,
    instrument_alias,
    instrument_annotation,
    link_type,
    instrument_tag,
    instrument_tag_raw,
    iso_3166_1,
    iso_3166_2,
    iso_3166_3,
    isrc,
    iswc,
    link,
    l_area_area,
    l_area_artist,
    l_area_event,
    l_area_instrument,
    l_area_label,
    l_area_place,
    l_area_recording,
    l_area_release,
    l_area_release_group,
    l_area_series,
    l_area_url,
    l_area_work,
    l_artist_artist,
    l_artist_event,
    l_artist_instrument,
    l_artist_label,
    l_artist_place,
    l_artist_recording,
    l_artist_release,
    l_artist_release_group,
    l_artist_series,
    l_artist_url,
    l_artist_work,
    l_event_event,
    l_event_instrument,
    l_event_label,
    l_event_place,
    l_event_recording,
    l_event_release,
    l_event_release_group,
    l_event_series,
    l_event_url,
    l_event_work,
    l_label_label,
    l_instrument_instrument,
    l_instrument_label,
    l_instrument_place,
    l_instrument_recording,
    l_instrument_release,
    l_instrument_release_group,
    l_instrument_series,
    l_instrument_url,
    l_instrument_work,
    l_label_place,
    l_label_recording,
    l_label_release,
    l_label_release_group,
    l_label_series,
    l_label_url,
    l_label_work,
    l_place_place,
    l_place_recording,
    l_place_release,
    l_place_release_group,
    l_place_series,
    l_place_url,
    l_place_work,
    l_recording_recording,
    l_recording_release,
    l_recording_release_group,
    l_recording_series,
    l_recording_url,
    l_recording_work,
    l_release_release,
    l_release_release_group,
    l_release_series,
    l_release_url,
    l_release_work,
    l_release_group_release_group,
    l_release_group_series,
    l_release_group_url,
    l_release_group_work,
    l_series_series,
    l_series_url,
    l_series_work,
    l_url_url,
    l_url_work,
    l_work_work,
    vote,
    label_rating_raw,
    recording_rating_raw,
    label_tag_raw,
    label_alias_type,
    label_alias,
    label_annotation,
    label_ipi,
    label_isni,
    label_meta,
    recording_meta,
    work_meta,
    label_gid_redirect,
    place_gid_redirect,
    recording_gid_redirect,
    release_gid_redirect,
    release_group_gid_redirect,
    series_gid_redirect,
    track_gid_redirect,
    url_gid_redirect,
    work_gid_redirect,
    label_tag,
    place_tag,
    recording_tag,
    release_tag,
    release_group_tag,
    series_tag,
    work_tag,
    link_attribute,
    link_creditable_attribute_type,
    link_attribute_credit,
    link_attribute_text_value,
    link_type_attribute_type,
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
    editor_collection_work,
    editor_collection_deleted_entity,
    place_alias_type,
    recording_alias_type,
    release_alias_type,
    release_group_alias_type,
    series_alias_type,
    work_alias_type,
    place_alias,
    editor_oauth_token,
    editor_watch_preferences,
    editor_watch_artist,
    editor_watch_release_group_type,
    editor_watch_release_status,
    medium_cdtoc,
    orderable_link_type,
    place_annotation,
    place_tag_raw,
    recording_tag_raw,
    release_tag_raw,
    release_group_tag_raw,
    series_tag_raw,
    work_tag_raw,
    replication_control,
    recording_alias,
    release_alias,
    release_group_alias,
    series_alias,
    work_alias,
    recording_annotation,
    release_annotation,
    release_group_annotation,
    series_annotation,
    work_annotation,
    tag_relation,
    track_raw,
    medium_index,
    release_group_rating_raw,
    work_rating_raw,
    release_country,
    release_unknown_country,
    release_meta,
    release_coverart,
    release_label,
    release_group_meta,
    release_group_secondary_type_join,
    work_attribute_type,
    work_attribute_type_allowed_value,
    work_attribute,
    work_language,
    old_editor_name,
    area_attribute_type,
    artist_attribute_type,
    event_attribute_type,
    instrument_attribute_type,
    label_attribute_type,
    medium_attribute_type,
    place_attribute_type,
    recording_attribute_type,
    release_attribute_type,
    release_group_attribute_type,
    series_attribute_type,
    area_attribute_type_allowed_value,
    artist_attribute_type_allowed_value,
    event_attribute_type_allowed_value,
    instrument_attribute_type_allowed_value,
    label_attribute_type_allowed_value,
    medium_attribute_type_allowed_value,
    place_attribute_type_allowed_value,
    recording_attribute_type_allowed_value,
    release_attribute_type_allowed_value,
    release_group_attribute_type_allowed_value,
    series_attribute_type_allowed_value,
    area_attribute,
    artist_attribute,
    medium_attribute_type_allowed_format,
    medium_attribute_type_allowed_value_allowed_format,
    event_attribute,
    instrument_attribute,
    label_attribute,
    medium_attribute,
    place_attribute,
    recording_attribute,
    release_attribute,
    release_group_attribute,
    series_attribute,
]
