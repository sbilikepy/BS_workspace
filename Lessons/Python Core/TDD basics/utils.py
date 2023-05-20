def add_css_classes(element: dict, class_to_add: str) -> None:
    classes = dict.fromkeys(element["class_name"].split())
    classes[class_to_add] = None
    element["class_name"] = " ".join(classes.keys())


def remove_css_classes(element: dict, class_to_remove: str) -> None:
    classes = dict.fromkeys(element["class_name"].split())
    if class_to_remove in classes:
        del classes[class_to_remove]
    element["class_name"] = " ".join(classes.keys())
