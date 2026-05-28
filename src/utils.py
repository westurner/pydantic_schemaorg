"""Utilities for dynamic model building and lazy type resolution in pydantic_schemaorg.

This module provides infrastructure for handling the deeply cyclical Schema.org type graph,
including lazy namespace resolution, model schema rebuilding, and transitive type discovery.
Uses iterative stack-based traversal instead of recursion to avoid stack depth issues.
"""

from collections import deque
from datetime import time, datetime, date
from decimal import Decimal
from typing import Any, Optional, List, Union, Literal, Set, Type
import sys
import re

from pydantic import (
    BaseModel,
    StrictBool,
    AnyUrl,
    StrictInt,
    StrictFloat,
)

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic_schemaorg.__types__ import types


# Note: Pydantic v2's schema generation for deeply nested models internally uses recursion.
# While our rebuild logic and get_transitive_referenced_types use iterative stack-based
# traversal, Pydantic's own schema generation for complex unions/nested models can exceed
# Python's default recursion limit. This is a necessary safety net for Pydantic's internal
# schema building, not for our code.
sys.setrecursionlimit(max(sys.getrecursionlimit(), 5000))


_rebuilding: Set[Type[BaseModel]] = set()
_rebuilt: Set[Type[BaseModel]] = set()


class LazyTypeNamespace(dict):
    """A lazy-loading dictionary namespace for resolving Schema.org type references on demand.
    
    This dict subclass intercepts missing keys and dynamically imports the corresponding
    type from the pydantic_schemaorg package using the types registry. This allows circular
    imports to be resolved at runtime without requiring all types to be imported upfront.
    
    Attributes:
        initial_dict (dict): The initial mapping of names to values.
    """
    
    def __init__(self, initial_dict: dict) -> None:
        """Initialize the lazy namespace with an initial dictionary.
        
        Args:
            initial_dict: Initial key-value mappings to store in the namespace.
        """
        super().__init__(initial_dict)

    def __missing__(self, key: str) -> Any:
        """Load and return a type from the pydantic_schemaorg package by name.
        
        Args:
            key: The type name to load (e.g., 'Thing', 'Organization').
            
        Returns:
            The loaded type/class object.
            
        Raises:
            KeyError: If the key is not in the types registry.
            Exception: If importing the type fails (printed to stderr with traceback).
        """
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

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value by key, returning a default if not found.
        
        Args:
            key: The key to look up.
            default: The value to return if key is not found. Defaults to None.
            
        Returns:
            The value associated with key, or default if not found.
        """
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key: str) -> bool:
        """Check if a key is available in the namespace or types registry.
        
        Args:
            key: The key to check.
            
        Returns:
            True if the key is in the dict or in the types registry.
        """
        return super().__contains__(key) or key in types


def get_referenced_types(cls: Type[BaseModel]) -> Set[str]:
    """Extract Schema.org type names referenced in a class's annotations.
    
    Scans both the class's __annotations__ and model_fields to find all references
    to types that are registered in the Schema.org types registry.
    
    Args:
        cls: The class to inspect for type references.
        
    Returns:
        A set of type names (strings) that are referenced in the class.
    """
    referenced: Set[str] = set()
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


def get_transitive_referenced_types(
    cls: Type[BaseModel], visited: Optional[Set[Type[BaseModel]]] = None
) -> Set[str]:
    """Find all types transitively referenced by a class using iterative traversal.
    
    Uses a stack-based approach to traverse the full dependency graph of type references,
    collecting all types that the given class depends on, directly or indirectly.
    No recursion is used, avoiding stack depth limitations.
    
    Args:
        cls: The class to start the traversal from.
        visited: Set of already-visited classes (used for tracking). Defaults to None.
        
    Returns:
        A set of all type names (strings) transitively referenced by the class.
    """
    work_stack: List[Type[BaseModel]] = [cls]
    visited_classes: Set[Type[BaseModel]] = visited if visited is not None else set()
    all_referenced_names: Set[str] = set()
    
    while work_stack:
        current_cls = work_stack.pop()
        if current_cls in visited_classes:
            continue
        visited_classes.add(current_cls)
        
        # Get direct type references for this class
        referenced_names = get_referenced_types(current_cls)
        all_referenced_names.update(referenced_names)
        
        # Add referenced type classes to the work stack for processing
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
                    if type_class and type_class not in visited_classes:
                        work_stack.append(type_class)
    
    return all_referenced_names


def rebuild_model(cls: Type[BaseModel], **kwargs: Any) -> None:
    """Rebuild a Pydantic model schema with lazy type resolution and transitive dependencies.
    
    This function handles the complex schema rebuilding for Schema.org models, ensuring
    that all transitive type dependencies are available and properly injected into the
    model's namespace. It prevents infinite recursion by tracking rebuilding and rebuilt
    classes globally.
    
    Args:
        cls: The Pydantic model class to rebuild.
        *args: Positional arguments to pass to BaseModel.model_rebuild().
        **kwargs: Keyword arguments to pass to BaseModel.model_rebuild().
    """
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
            from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
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
        # Call BaseModel's model_rebuild method directly through the MRO to bypass our override
        # Find the first parent class with model_rebuild and call its version
        for parent in type(cls).__mro__[1:]:
            if 'model_rebuild' in parent.__dict__:
                parent.model_rebuild(cls, **kwargs)
                break
        _rebuilt.add(cls)
    finally:
        _rebuilding.discard(cls)
