from pydantic_schemaorg.WebPage import WebPage
import re
for k, prop in WebPage.model_fields.items():
    if prop.annotation:
        print(repr(str(prop.annotation)))
        print(re.findall(r"'([A-Za-z0-9_]+)'", str(prop.annotation)))
        break
