import time
from unittest import mock

import pytest

from mock.main import delay


@pytest.fixture()
def mocked_sleep():
    with mock.patch("time.sleep") as mocked_test_sleep:
        yield mocked_test_sleep


def test_ret_foo_value(mocked_sleep):
    assert delay(2, lambda: 10) == 10


def test_foo_was_called(mocked_sleep):
    # def mock_function():
    #     mock_function.has_been_called = True
    #
    # mock_function.has_been_called = False
    # assert mock_function.has_been_called
    mock_function = mock.MagicMock()

    delay(3, mock_function)

    mock_function.assert_called_once()


def test_sleep(mocked_sleep):
    # time.sleep = mock.MagicMock()

    # with mock.patch("time.sleep") as mocked_sleep:
    #     delay(100, lambda: None)
    delay(100, lambda: None)
    mocked_sleep.assert_called_once_with(100)
    # time.sleep.assert_called_once_with(100)
