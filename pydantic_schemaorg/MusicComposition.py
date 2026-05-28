from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicComposition(CreativeWork):
    """A musical composition.

    See: https://schema.org/MusicComposition
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MusicComposition"
    type_: str = Field("MusicComposition", alias='@type')
    musicCompositionForm: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type of composition (e.g. overture, sonata, symphony, etc.).",
    )
    lyricist: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The person who wrote the words.",
    )
    musicArrangement: Optional[Union[List[Union['MusicComposition', str]], 'MusicComposition', str]] = Field(
        default=None,
        description="An arrangement derived from the composition.",
    )
    iswcCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The International Standard Musical Work Code for the composition.",
    )
    musicalKey: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The key, mode, or scale this composition uses.",
    )
    recordedAs: Optional[Union[List[Union['MusicRecording', str]], 'MusicRecording', str]] = Field(
        default=None,
        description="An audio recording of the work.",
    )
    includedComposition: Optional[Union[List[Union['MusicComposition', str]], 'MusicComposition', str]] = Field(
        default=None,
        description="Smaller compositions included in this work (e.g. a movement in a symphony).",
    )
    firstPerformance: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="The date and place the work was first performed.",
    )
    lyrics: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="The words in the song.",
    )
    composer: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed"
     "at some event.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Organization import Organization


def __getattr__(name: str) -> Any:
    from pydantic_schemaorg.__types__ import types
    if name in types:
        import sys
        mod_name = types[name][1]
        mod = sys.modules.get(mod_name)
        if not mod:
            __import__(mod_name, fromlist=[name])
            mod = sys.modules[mod_name]
        val = getattr(mod, name)
        globals()[name] = val
        return val
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
