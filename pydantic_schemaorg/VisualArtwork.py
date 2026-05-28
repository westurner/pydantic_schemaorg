from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class VisualArtwork(CreativeWork):
    """A work of art that is primarily visual in character.

    See: https://schema.org/VisualArtwork
    Model depth: 3
    """
    valid_name: ClassVar[str] = "VisualArtwork"
    type_: str = Field("VisualArtwork", alias='@type')
    artist: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The primary artist for a work in a medium other than pencils or digital line art--for example,"
     "if the primary artwork is done in watercolors or digital paints.",
    )
    penciler: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who draws the primary narrative artwork.",
    )
    artEdition: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="The number of copies when multiple copies of a piece of artwork are produced - e.g. for"
     "a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in"
     "this example \"20\").",
    )
    height: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    artMedium: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The material used. (E.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype,"
     "Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)",
    )
    surface: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="A material used as a surface in some artwork, e.g. Canvas, Paper, Wood, Board, etc.",
    )
    width: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The width of the item.",
    )
    artworkSurface: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.",
    )
    letterer: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who adds lettering, including speech balloons and sound effects, to"
     "artwork.",
    )
    depth: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The depth of the item.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', 'Mass', str]], 'QuantitativeValue', 'Mass', str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    colorist: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who adds color to inked drawings.",
    )
    inker: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who traces over the pencil drawings in ink after pencils are complete.",
    )
    artform: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Mass import Mass


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
