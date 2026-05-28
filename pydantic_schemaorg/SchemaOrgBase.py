from datetime import time, datetime, date
from decimal import Decimal
from typing import Any, Optional, ForwardRef, List, Union, Literal
import sys
import re

from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    AnyUrl,
    StrictInt,
    StrictFloat,
    ConfigDict,
)

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic_schemaorg.__types__ import types

_rebuilding = set()
_rebuilt = set()

# Schema.org models have a very deep cyclical graph. Pydantic schema generation
# can legitimately exceed Python's default recursion limit.
sys.setrecursionlimit(max(sys.getrecursionlimit(), 10000))


class LazyTypeNamespace(dict):
    def __init__(self, initial_dict):
        super().__init__(initial_dict)

    def __getitem__(self, key):
        if super().__contains__(key):
            return super().__getitem__(key)
        if key in types:
            mod_name = types[key][1]
            try:
                mod = sys.modules.get(mod_name)
                if not mod:
                    __import__(mod_name, fromlist=[key])
                    mod = sys.modules[mod_name]
                val = getattr(mod, key)
                self[key] = val
                return val
            except Exception as e:
                import traceback

                print(f"LazyTypeNamespace error importing {key}: {e}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                raise
        raise KeyError(key)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return super().__contains__(key) or key in types


class SchemaOrgBase(BaseModel):
    # JSON-LD fields
    reverse_: Optional[Any] = Field(default=None, alias="@reverse")
    id_: Optional[Any] = Field(default=None, alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    def dict(self, *args, **kwargs):
        defaults = {"exclude_none": True, "by_alias": True}
        return super().dict(*args, **dict(defaults, **kwargs))

    def json(self, *args, **kwargs):
        defaults = {"exclude_none": True, "by_alias": True}
        return super().json(*args, **dict(defaults, **kwargs))

    model_config = ConfigDict(populate_by_name=True)

    @classmethod
    def _get_referenced_types(cls):
        """Extract type names from class annotations."""
        referenced = set()
        # Check __annotations__ which preserves original string representations
        for ann in getattr(cls, "__annotations__", {}).values():
            ann_str = str(ann)
            for match in re.finditer(r"'([^']+)'|(?<!\w)([A-Z]\w+)(?!\w)", ann_str):
                name = match.group(1) or match.group(2)
                if name in types:
                    referenced.add(name)
        # Fallback to model_fields in case of dynamically injected/modified fields
        for k, v in cls.model_fields.items():
            if v.annotation:
                ann_str = str(v.annotation)
                for match in re.finditer(r"'([^']+)'|(?<!\w)([A-Z]\w+)(?!\w)", ann_str):
                    name = match.group(1) or match.group(2)
                    if name in types:
                        referenced.add(name)
        return referenced

    @classmethod
    def _get_transitive_referenced_types(cls, visited=None):
        if visited is None:
            visited = set()
        if cls in visited:
            return set()
        visited.add(cls)

        referenced_names = cls._get_referenced_types()
        all_referenced_names = set(referenced_names)

        import sys

        for ref in referenced_names:
            if ref in types:
                mod_name = types[ref][1]
                if mod_name not in sys.modules:
                    try:
                        __import__(mod_name, fromlist=[ref])
                    except Exception:
                        continue
                mod = sys.modules.get(mod_name)
                if mod:
                    type_class = getattr(mod, ref, None)
                    if type_class and hasattr(
                        type_class, "_get_transitive_referenced_types"
                    ):
                        all_referenced_names.update(
                            type_class._get_transitive_referenced_types(visited)
                        )
        return all_referenced_names

    @classmethod
    def model_rebuild(cls, *args, **kwargs: Any) -> None:
        if cls in _rebuilding:
            return
        if cls in _rebuilt:
            return
        _rebuilding.add(cls)

        try:
            local_classes = {
                "AnyUrl": AnyUrl,
                "Decimal": Decimal,
                "ISO8601Date": ISO8601Date,
                "List": List,
                "Literal": Literal,
                "Optional": Optional,
                "StrictBool": StrictBool,
                "StrictFloat": StrictFloat,
                "StrictInt": StrictInt,
                "Union": Union,
                "date": date,
                "datetime": datetime,
                "time": time,
            }

            # Get transitive web of referenced type names
            all_referenced_names = set()
            for c in cls.mro():
                if issubclass(c, SchemaOrgBase) and c is not SchemaOrgBase:
                    if hasattr(c, "_get_transitive_referenced_types"):
                        all_referenced_names.update(c._get_transitive_referenced_types())

            import sys

            # First, ensure all transitive references are in local_classes (our parent namespace)
            for ref in all_referenced_names:
                if ref in types:
                    mod_name = types[ref][1]
                    mod = sys.modules.get(mod_name)
                    if not mod:
                        try:
                            __import__(mod_name, fromlist=[ref])
                            mod = sys.modules.get(mod_name)
                        except Exception:
                            continue
                    if mod:
                        type_class = getattr(mod, ref, None)
                        if type_class:
                            local_classes[ref] = type_class

            # Second, for each transitive reference module, inject standard helpers and its own direct references
            for ref in all_referenced_names:
                if ref in types:
                    mod_name = types[ref][1]
                    mod = sys.modules.get(mod_name)
                    if mod:
                        type_class = getattr(mod, ref, None)
                        if type_class:
                            mod_dict = mod.__dict__
                            # Inject standard helpers
                            for helper_name, helper_val in local_classes.items():
                                if helper_name not in mod_dict:
                                    mod_dict[helper_name] = helper_val
                            # Inject direct references
                            if hasattr(type_class, "_get_referenced_types"):
                                for direct_ref in type_class._get_referenced_types():
                                    if direct_ref in types:
                                        dr_mod_name = types[direct_ref][1]
                                        dr_mod = sys.modules.get(dr_mod_name)
                                        if not dr_mod:
                                            try:
                                                __import__(dr_mod_name, fromlist=[direct_ref])
                                                dr_mod = sys.modules.get(dr_mod_name)
                                            except Exception:
                                                continue
                                        if dr_mod:
                                            dr_class = getattr(dr_mod, direct_ref, None)
                                            if dr_class and direct_ref not in mod_dict:
                                                mod_dict[direct_ref] = dr_class

            kwargs.setdefault("_types_namespace", LazyTypeNamespace(local_classes))
            super().model_rebuild(*args, **kwargs)
            _rebuilt.add(cls)
        finally:
            _rebuilding.discard(cls)

    def __init__(__pydantic_self__, **data: Any) -> None:
        type(__pydantic_self__).model_rebuild()
        super().__init__(**data)

