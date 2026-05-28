from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import datetime, time
from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Action(Thing):
    """An action performed by a direct agent and indirect participants upon a direct object."
     "Optionally happens at a location with the help of an inanimate instrument. The execution"
     "of the action may produce a result. Specific action sub-type documentation specifies"
     "the exact expectation of each argument/role. See also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html)"
     "and [Actions overview document](https://schema.org/docs/actions.html).

    See: https://schema.org/Action
    Model depth: 2
    """
    valid_name: ClassVar[str] = "Action"
    type_: str = Field("Action", alias='@type')
    startTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    actionStatus: Optional[Union[List[Union['ActionStatusType', str]], 'ActionStatusType', str]] = Field(
        default=None,
        description="Indicates the current disposition of the Action.",
    )
    object: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The object upon which the action is carried out, whose state is kept intact or changed."
     "Also known as the semantic roles patient, affected or undergoer (which change their"
     "state) or theme (which doesn't). E.g. John read *a book*.",
    )
    actionProcess: Optional[Union[List[Union['HowTo', str]], 'HowTo', str]] = Field(
        default=None,
        description="Description of the process by which the action was performed.",
    )
    target: Optional[Union[List[Union[AnyUrl, 'URL', 'EntryPoint', str]], AnyUrl, 'URL', 'EntryPoint', str]] = Field(
        default=None,
        description="Indicates a target EntryPoint, or url, for an Action.",
    )
    location: Optional[Union[List[Union[str, 'Text', 'VirtualLocation', 'PostalAddress', 'Place']], str, 'Text', 'VirtualLocation', 'PostalAddress', 'Place']] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    instrument: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.",
    )
    endTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    result: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The result produced in the action. E.g. John wrote *a book*.",
    )
    error: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="For failed actions, more information on the cause of the failure.",
    )
    participant: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="Other co-agents that participated in the action indirectly. E.g. John wrote a book with"
     "*Steve*.",
    )
    agent: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote"
     "a book.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.ActionStatusType import ActionStatusType
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.HowTo import HowTo
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.EntryPoint import EntryPoint
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Place import Place


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
