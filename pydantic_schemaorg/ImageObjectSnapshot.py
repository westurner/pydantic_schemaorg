from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.ImageObject import ImageObject


class ImageObjectSnapshot(ImageObject):
    """A specific and exact (byte-for-byte) version of an [[ImageObject]]. Two byte-for-byte"
     "identical files, for the purposes of this type, considered identical. If they have different"
     "embedded metadata (e.g. XMP, EXIF) the files will differ. Different external facts"
     "about the files, e.g. creator or dateCreated that aren't represented in their actual"
     "content, do not affect this notion of identity.

    See: https://schema.org/ImageObjectSnapshot
    Model depth: 5
    """
    valid_name: ClassVar[str] = "ImageObjectSnapshot"
    type_: str = Field("ImageObjectSnapshot", alias='@type')
    



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
