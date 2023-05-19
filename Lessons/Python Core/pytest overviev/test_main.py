# pytest_overview
# function - based
from main import add, subtract


def test_can_add_2_numbers():
    assert add(1, 1) == 2


def test_can_sub_2_numbers():
    assert subtract(1, 1) == 0
