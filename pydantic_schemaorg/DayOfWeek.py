from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class DayOfWeek(Enumeration):
    """The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification"
     "refer. Originally, URLs from [GoodRelations](http://purl.org/goodrelations/v1)"
     "were used (for [[Monday]], [[Tuesday]], [[Wednesday]], [[Thursday]], [[Friday]],"
     "[[Saturday]], [[Sunday]] plus a special entry for [[PublicHolidays]]); these have"
     "now been integrated directly into schema.org.

    See: https://schema.org/DayOfWeek
    Model depth: 4
    """
    valid_name: ClassVar[str] = "DayOfWeek"
    type_: str = Field("DayOfWeek", alias='@type')
    



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
