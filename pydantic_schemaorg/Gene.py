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
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class Gene(BioChemEntity):
    """A discrete unit of inheritance which affects one or more biological traits (Source:"
     "[https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene))."
     "Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific"
     "RNA 21), A- (agouti genotype).

    See: https://schema.org/Gene
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Gene"
    type_: str = Field("Gene", alias='@type')
    encodesBioChemEntity: Optional[Union[List[Union['BioChemEntity', str]], 'BioChemEntity', str]] = Field(
        default=None,
        description="Another BioChemEntity encoded by this one.",
    )
    expressedIn: Optional[Union[List[Union['BioChemEntity', 'DefinedTerm', 'AnatomicalSystem', 'AnatomicalStructure', str]], 'BioChemEntity', 'DefinedTerm', 'AnatomicalSystem', 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Tissue, organ, biological sample, etc in which activity of this gene has been observed"
     "experimentally. For example brain, digestive system.",
    )
    alternativeOf: Optional[Union[List[Union['Gene', str]], 'Gene', str]] = Field(
        default=None,
        description="Another gene which is a variation of this one.",
    )
    hasBioPolymerSequence: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A symbolic representation of a BioChemEntity. For example, a nucleotide sequence of"
     "a Gene or an amino acid sequence of a Protein.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.BioChemEntity import BioChemEntity
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.Text import Text


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
