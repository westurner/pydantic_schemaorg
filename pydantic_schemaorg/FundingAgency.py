from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Project import Project


class FundingAgency(Project):
    """A FundingAgency is an organization that implements one or more [[FundingScheme]]s"
     "and manages the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s)."
     "A funding agency is not always required for grant funding, e.g. philanthropic giving,"
     "corporate sponsorship etc. Examples of funding agencies include ERC, REA, NIH, Bill"
     "and Melinda Gates Foundation, ...

    See: https://schema.org/FundingAgency
    Model depth: 4
    """
    valid_name: ClassVar[str] = "FundingAgency"
    type_: str = Field("FundingAgency", alias='@type')
    



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
