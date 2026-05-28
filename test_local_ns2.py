from pydantic_schemaorg.WebPage import WebPage
for k, prop in WebPage.model_fields.items():
    print(k, ":", repr(prop.annotation))
