from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ProfessionalService(LocalBusiness):
    """Original definition: \"provider of professional services.\" The general [[ProfessionalService]]"
     "type for local businesses was deprecated due to confusion with [[Service]]. For reference,"
     "the types that it included were: [[Dentist]], [[AccountingService]], [[Attorney]],"
     "[[Notary]], as well as types for several kinds of [[HomeAndConstructionBusiness]]:"
     "[[Electrician]], [[GeneralContractor]], [[HousePainter]], [[Locksmith]], [[Plumber]],"
     "[[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive supertype"
     "of [[Attorney]].

    See: https://schema.org/ProfessionalService
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ProfessionalService"
    type_: str = Field("ProfessionalService", alias='@type')
    



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
