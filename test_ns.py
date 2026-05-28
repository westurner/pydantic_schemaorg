from pydantic._internal._typing_extra import NsResolver
ns = NsResolver(parent_namespace={'A': 1}, types_namespace={'B': 2})
print(ns.types_namespace)
