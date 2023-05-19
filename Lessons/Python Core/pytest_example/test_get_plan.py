import pytest
from get_plan import get_plan


def test_should_return_list():
    goals = get_plan(500, 3, 50)
    assert isinstance(goals, list)


def test_should_return_list_of_given_length():
    goals = get_plan(500, 3, 50)
    assert len(goals) == 3


def test_should_return_expected_goals_with_rounding():
    goals = get_plan(500, 3, 50)
    assert goals == [750, 1125, 1687]


def test_should_return_expected_goals_without_rounding():
    goals = get_plan(100, 4, 100)
    assert goals == [200, 400, 800, 1600]
