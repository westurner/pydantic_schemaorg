from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Taxon(Thing):
    """A set of organisms asserted to represent a natural cohesive biological unit.

    See: https://schema.org/Taxon
    Model depth: 2
    """
    valid_name: ClassVar[str] = "Taxon"
    type_: str = Field("Taxon", alias='@type')
    taxonRank: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'PropertyValue']], AnyUrl, 'URL', str, 'Text', 'PropertyValue']] = Field(
        default=None,
        description="The taxonomic rank of this taxon given preferably as a URI from a controlled vocabulary"
     "– typically the ranks from TDWG TaxonRank ontology or equivalent Wikidata URIs.",
    )
    parentTaxon: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Taxon']], AnyUrl, 'URL', str, 'Text', 'Taxon']] = Field(
        default=None,
        description="Closest parent taxon of the taxon in question.",
    )
    hasDefinedTerm: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="A Defined Term contained in this term set.",
    )
    childTaxon: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Taxon']], AnyUrl, 'URL', str, 'Text', 'Taxon']] = Field(
        default=None,
        description="Closest child taxa of the taxon in question.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.DefinedTerm import DefinedTerm


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
