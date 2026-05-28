from pydantic_schemaorg.WebPage import WebPage
field = WebPage.model_fields['significantLink']
print(repr(field.annotation))
print(type(field.annotation))

import re
print("Using regex:", re.findall(r"'([A-Za-z0-9_]+)'", str(field.annotation)))
