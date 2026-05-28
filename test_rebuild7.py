from pydantic_schemaorg.WebPage import WebPage
try:
    WebPage.model_rebuild()
except Exception:
    pass

print(type(getattr(WebPage, "__pydantic_parent_namespace__", None)))
