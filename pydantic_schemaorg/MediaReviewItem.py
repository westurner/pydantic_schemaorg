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


class MediaReviewItem(CreativeWork):
    """Represents an item or group of closely related items treated as a unit for the sake of evaluation"
     "in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping"
     "or reviewing party.

    See: https://schema.org/MediaReviewItem
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MediaReviewItem"
    type_: str = Field("MediaReviewItem", alias='@type')
    mediaItemAppearance: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        default=None,
        description="In the context of a [[MediaReview]], indicates specific media item(s) that are grouped"
     "using a [[MediaReviewItem]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MediaObject import MediaObject


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
