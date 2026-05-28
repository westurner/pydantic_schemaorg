from pydantic_schemaorg.WebPage import WebPage
import re
prop = WebPage.model_fields['significantLink']
print(repr(str(prop.annotation)))
print(re.findall(r"'([A-Za-z0-9_]+)'", str(prop.annotation)))
