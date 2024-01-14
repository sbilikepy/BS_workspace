import pytest

from utils import add_css_classes


class TestAddCssClass:
    @pytest.mark.parametrize(
        "initial_classes, class_to_add, expected_classes",
        [
            pytest.param(
                "joke new", "active", "joke new active", id="should add new classes"
            ),
            pytest.param(
                "joke new", "new", "joke new", id="should not add existing classes"
            ),
            pytest.param(
                "joke new active",
                "ok",
                "joke new active ok",
                id="should add class which is part of another one",
            ),
        ],
    )
    def test_modify_classes_correctly(
        self, initial_classes, class_to_add, expected_classes
    ):
        el = {"classes": initial_classes}

        add_css_classes(el, class_to_add)

        assert el["classes"] == expected_classes


# class TestRemoveCssClass:
#     def test_should_remove_existing_css_class(self):
#         el = {
#             "classes": "joke new",
#         }
#         remove_css_classes(el, "joke")
#
#         assert el["classes"] == "new"
#
#     def test_should_remove_extra_spaces(self):
#         el = {
#             "classes": "  joke  new ",
#         }
#         remove_css_classes(el, "joke")
#
#         assert el["classes"] == "new"
#
#     def test_should_remove_all_occurrences(self):
#         el = {
#             "classes": "joke new joke new joke new",
#         }
#         remove_css_classes(el, "joke")
#
#         assert el["classes"] == "new"
#
#     def test_should_remove_duplicates_of_other_classes(self):
#         el = {
#             "classes": "hello new hello new",
#         }
#         remove_css_classes(el, "joke")
#
#         assert el["classes"] == "hello new"
