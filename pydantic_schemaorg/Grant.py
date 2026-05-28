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
from pydantic_schemaorg.Intangible import Intangible


class Grant(Intangible):
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a"
     "[[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],"
     "sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in"
     "one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]]"
     "of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s"
     "of resources (e.g. office space). Grants support activities directed towards some"
     "agreed collective goals, often but not always organized as [[Project]]s. Long-lived"
     "projects are sometimes sponsored by a variety of grants over time, but it is also common"
     "for a project to be associated with a single grant. The amount of a [[Grant]] is represented"
     "using [[amount]] as a [[MonetaryAmount]].

    See: https://schema.org/Grant
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Grant"
    type_: str = Field("Grant", alias='@type')
    fundedItem: Optional[Union[List[Union['Product', 'Organization', 'MedicalEntity', 'BioChemEntity', 'CreativeWork', 'Event', 'Person', str]], 'Product', 'Organization', 'MedicalEntity', 'BioChemEntity', 'CreativeWork', 'Event', 'Person', str]] = Field(
        default=None,
        description="Indicates something directly or indirectly funded or sponsored through a [[Grant]]."
     "See also [[ownershipFundingInfo]].",
    )
    sponsor: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    funder: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.BioChemEntity import BioChemEntity
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Person import Person


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
