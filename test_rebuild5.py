from pydantic_schemaorg.WebPage import WebPage
print("local_classes for WebPage:")
from pydantic_schemaorg import __types__
import importlib, re
localns = {}
for prop in WebPage.model_fields.values():
    if prop.annotation:
        refs = re.findall(r"'([A-Za-z0-9_]+)'", str(prop.annotation))
        for ref in refs:
            if ref in __types__.types:
                mod_name = __types__.types[ref][1]
                mod = importlib.import_module(mod_name)
                localns[ref] = getattr(mod, ref)
print(list(localns.keys()))
