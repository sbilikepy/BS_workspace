from utils import add_css_classes, remove_css_classes


class TestAddCssClass:
    def test_should_add_new_class(self):
        el = {
            "class_name": "joke new",
        }
        add_css_classes(el, "active")

        assert el["class_name"] == "joke new active"

    def test_should_not_add_existing_class(self):
        # preparation
        el = {
            "class_name": "joke new",
        }
        # action
        add_css_classes(el, "new")
        # check
        assert el["class_name"] == "joke new"

    def test_should_add_class_which_is_part_of_another_one(self):
        el = {
            "class_name": "joke new active",
        }
        add_css_classes(el, "ok")

        assert el["class_name"] == "joke new active ok"

    def test_should_remove_extra_outer_spaces(self):
        el = {
            "class_name": "   joke new  ",
        }
        add_css_classes(el, "active")

        assert el["class_name"] == "joke new active"

    def test_should_remove_extra_inner_spaces(self):
        el = {
            "class_name": "joke      new"
        }
        add_css_classes(el, "active")

        assert el["class_name"] == "joke new active"

    def test_should_remove_extra_spaces_when_new_class_not_added(self):
        el = {
            "class_name": " joke      new  active "
        }
        add_css_classes(el, "active")

        assert el["class_name"] == "joke new active"

    def test_should_remove_duplicates(self):
        el = {
            "class_name": "   joke new joke new new ",
        }
        add_css_classes(el, "active")

        assert el["class_name"] == "joke new active"


class TestRemoveCssClass:
    def test_should_remove_existing_css_class(self):
        el = {
            "class_name": "joke new",
        }
        remove_css_classes(el, "joke")

        assert el["class_name"] == "new"

    def test_should_remove_extra_spaces(self):
        el = {
            "class_name": "  joke  new ",
        }
        remove_css_classes(el, "joke")

        assert el["class_name"] == "new"

    def test_should_remove_all_occurrences(self):
        el = {
            "class_name": "joke new joke new joke new",
        }
        remove_css_classes(el, "joke")

        assert el["class_name"] == "new"

    def test_should_remove_duplicates_of_other_classes(self):
        el = {
            "class_name": "hello new hello new",
        }
        remove_css_classes(el, "joke")

        assert el["class_name"] == "hello new"
