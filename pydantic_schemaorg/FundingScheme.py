from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class FundingScheme(Organization):
    """A FundingScheme combines organizational, project and policy aspects of grant-based"
     "funding that sets guidelines, principles and mechanisms to support other kinds of projects"
     "and activities. Funding is typically organized via [[Grant]] funding. Examples of"
     "funding schemes: Swiss Priority Programmes (SPPs); EU Framework 7 (FP7); Horizon 2020;"
     "the NIH-R01 Grant Program; Wellcome institutional strategic support fund. For large"
     "scale public sector funding, the management and administration of grant awards is often"
     "handled by other, dedicated, organizations - [[FundingAgency]]s such as ERC, REA,"
     "...

    See: https://schema.org/FundingScheme
    Model depth: 3
    """
    valid_name: ClassVar[str] = "FundingScheme"
    type_: str = Field("FundingScheme", alias='@type')
    



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
