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

# __ALL__ silences PEP8 `module imported but unused`:
__ALL__ = [
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
]
