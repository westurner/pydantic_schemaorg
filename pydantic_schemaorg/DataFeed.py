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
from pydantic_schemaorg.Dataset import Dataset


class DataFeed(Dataset):
    """A single feed providing structured information about one or more entities or topics.

    See: https://schema.org/DataFeed
    Model depth: 4
    """
    valid_name: ClassVar[str] = "DataFeed"
    type_: str = Field("DataFeed", alias='@type')
    dataFeedElement: Optional[Union[List[Union[str, 'Text', 'DataFeedItem', 'Thing']], str, 'Text', 'DataFeedItem', 'Thing']] = Field(
        default=None,
        description="An item within a data feed. Data feeds may have many elements.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DataFeedItem import DataFeedItem
    from pydantic_schemaorg.Thing import Thing


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
