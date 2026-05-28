from pydantic_schemaorg.WebPage import WebPage
print("is complete:", WebPage.__pydantic_complete__)
try:
    WebPage()
except Exception as e:
    print(e)
WebPage.model_rebuild()
