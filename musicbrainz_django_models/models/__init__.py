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
]
