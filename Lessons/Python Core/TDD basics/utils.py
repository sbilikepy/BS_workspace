def add_css_classes(element: dict, class_to_add: str) -> None:
    if not element["is_hidden"]:
        classes = dict.fromkeys(element["classes"].split())
        classes[class_to_add] = None
        element["classes"] = " ".join(classes.keys())


# def remove_css_classes(element: dict, class_to_remove: str) -> None:
#     classes = dict.fromkeys(element["classes"].split())
#     if class_to_remove in classes:
#         del classes[class_to_remove]
#     element["classes"] = " ".join(classes.keys())
