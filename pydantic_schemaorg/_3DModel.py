from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictBool
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class _3DModel(MediaObject):
    """A 3D model represents some kind of 3D content, which may have [[encoding]]s in one or more"
     "[[MediaObject]]s. Many 3D formats are available (e.g. see [Wikipedia](https://en.wikipedia.org/wiki/Category:3D_graphics_file_formats));"
     "specific encoding formats can be represented using the [[encodingFormat]] property"
     "applied to the relevant [[MediaObject]]. For the case of a single file published after"
     "Zip compression, the convention of appending '+zip' to the [[encodingFormat]] can"
     "be used. Geospatial, AR/VR, artistic/animation, gaming, engineering and scientific"
     "content can all be represented using [[3DModel]].

    See: https://schema.org/3DModel
    Model depth: 4
    """
    valid_name: ClassVar[str] = "_3DModel"
    type_: str = Field("3DModel", alias='@type')
    isResizable: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether the 3DModel allows resizing. For example, room layout applications often do"
     "not allow 3DModel elements to be resized to reflect reality.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean


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
