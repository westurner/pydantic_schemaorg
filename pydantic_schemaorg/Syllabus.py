from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LearningResource import LearningResource


class Syllabus(LearningResource):
    """A syllabus that describes the material covered in a course, often with several such sections"
     "per [[Course]] so that a distinct [[timeRequired]] can be provided for that section"
     "of the [[Course]].

    See: https://schema.org/Syllabus
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Syllabus"
    type_: str = Field("Syllabus", alias='@type')
    



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
