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
from pydantic_schemaorg.MedicalCondition import MedicalCondition


class InfectiousDisease(MedicalCondition):
    """An infectious disease is a clinically evident human disease resulting from the presence"
     "of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi,"
     "protozoa, multicellular parasites, and prions. To be considered an infectious disease,"
     "such pathogens are known to be able to cause this disease.

    See: https://schema.org/InfectiousDisease
    Model depth: 4
    """
    valid_name: ClassVar[str] = "InfectiousDisease"
    type_: str = Field("InfectiousDisease", alias='@type')
    infectiousAgentClass: Optional[Union[List[Union['InfectiousAgentClass', str]], 'InfectiousAgentClass', str]] = Field(
        default=None,
        description="The class of infectious agent (bacteria, prion, etc.) that causes the disease.",
    )
    infectiousAgent: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The actual infectious agent, such as a specific bacterium.",
    )
    transmissionMethod: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes"
     "aegypti', etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass
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
