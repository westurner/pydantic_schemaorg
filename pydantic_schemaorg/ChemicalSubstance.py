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


class ChemicalSubstance(BioChemEntity):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular"
     "entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

    See: https://schema.org/ChemicalSubstance
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ChemicalSubstance"
    type_: str = Field("ChemicalSubstance", alias='@type')
    potentialUse: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="Intended use of the BioChemEntity by humans.",
    )
    chemicalComposition: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The chemical composition describes the identity and relative ratio of the chemical"
     "elements that make up the substance.",
    )
    chemicalRole: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
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
