from pydantic_schemaorg.WebPage import WebPage
classes = {}
for k, v in WebPage.model_fields.items():
    cls_list = WebPage.get_classes_for_forward_ref(v)
    for class_name, class_ in cls_list:
        classes[class_name] = class_
print(classes.keys())
