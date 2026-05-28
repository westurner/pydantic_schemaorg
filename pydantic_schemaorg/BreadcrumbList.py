from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.ItemList import ItemList


class BreadcrumbList(ItemList):
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically"
     "described using at least their URL and their name, and typically ending with the current"
     "page. The [[position]] property is used to reconstruct the order of the items in a BreadcrumbList."
     "The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]]"
     "(lower values listed first), and that the first items in this list correspond to the \"top\""
     "or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific"
     "values of 'position' are not assigned meaning for a BreadcrumbList, but they should"
     "be integers, e.g. beginning with '1' for the first item in the list.

    See: https://schema.org/BreadcrumbList
    Model depth: 4
    """
    valid_name: ClassVar[str] = "BreadcrumbList"
    type_: str = Field("BreadcrumbList", alias='@type')
    



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
