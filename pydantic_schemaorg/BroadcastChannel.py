from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class BroadcastChannel(Intangible):
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

    See: https://schema.org/BroadcastChannel
    Model depth: 3
    """
    valid_name: ClassVar[str] = "BroadcastChannel"
    type_: str = Field("BroadcastChannel", alias='@type')
    inBroadcastLineup: Optional[Union[List[Union['CableOrSatelliteService', str]], 'CableOrSatelliteService', str]] = Field(
        default=None,
        description="The CableOrSatelliteService offering the channel.",
    )
    broadcastFrequency: Optional[Union[List[Union[str, 'Text', 'BroadcastFrequencySpecification']], str, 'Text', 'BroadcastFrequencySpecification']] = Field(
        default=None,
        description="The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g."
     "87-99. In addition a shortcut idiom is supported for frequencies of AM and FM radio channels,"
     "e.g. \"87 FM\".",
    )
    broadcastServiceTier: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type of service required to have access to the channel (e.g. Standard or Premium).",
    )
    providesBroadcastService: Optional[Union[List[Union['BroadcastService', str]], 'BroadcastService', str]] = Field(
        default=None,
        description="The BroadcastService offered on this channel.",
    )
    broadcastChannelId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unique address by which the BroadcastService can be identified in a provider lineup."
     "In US, this is typically a number.",
    )
    genre: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CableOrSatelliteService import CableOrSatelliteService
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BroadcastFrequencySpecification import BroadcastFrequencySpecification
    from pydantic_schemaorg.BroadcastService import BroadcastService
    from pydantic_schemaorg.URL import URL


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
