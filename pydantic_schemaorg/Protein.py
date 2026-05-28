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


class Protein(BioChemEntity):
    """Protein is here used in its widest possible definition, as classes of amino acid based"
     "molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB"
     "group) or even a single molecule that one can point to are all of type :Protein. A protein"
     "can thus be a subclass of another protein, e.g. :Protein as a UniProt record can have multiple"
     "isoforms inside it which would also be :Protein. They can be imagined, synthetic, hypothetical"
     "or naturally occurring.

    See: https://schema.org/Protein
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Protein"
    type_: str = Field("Protein", alias='@type')
    hasBioPolymerSequence: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A symbolic representation of a BioChemEntity. For example, a nucleotide sequence of"
     "a Gene or an amino acid sequence of a Protein.",
    )
    


if TYPE_CHECKING:
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
