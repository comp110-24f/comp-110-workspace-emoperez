"""Testing find_and_remove_max."""

__author__ = "730801797"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_value() -> None:
    x: list[int] = [6, 3, 9, 4, 9, 6]
    assert find_and_remove_max(x) == 9


def test_find_and_remove_max_mutate() -> None:
    x: list[int] = [6, 3, 9, 4, 9, 6]
    find_and_remove_max(x)
    assert x == [6, 3, 4, 6]


def test_find_and_remove_max_input() -> None:
    x: list[int] = []
    assert find_and_remove_max(x) == -1
