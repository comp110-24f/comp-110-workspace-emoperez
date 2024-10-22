"""Testing utils.py functions."""

__author__ = "730801797"

# The functions are being imported from utils.py
from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


def test_only_evens_mutate() -> None:
    """Checks to see that the inputted list wasn't mutated."""
    a: list[int] = [8, 2, 6, 7, 0, 1]
    assert a == [8, 2, 6, 7, 0, 1]


def test_only_evens_values() -> None:
    """Checks to see the function returns the correct value."""
    a: list[int] = [8, 2, 4, 0, 1, 3]
    assert only_evens(a) == [8, 2, 4, 0]


def test_only_evens_edge() -> None:
    """Checks to see if an empty list returns an expected empty list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_sub_mutate() -> None:
    """Checks to see that the inputted list wasn't mutated."""
    b: list[int] = [4, 5, 6, 7]
    x: int = 1
    y: int = 3
    sub(b, x, y)
    assert b == [4, 5, 6, 7]


def test_sub_values() -> None:
    """Checks to see that the function returns the expected value."""
    b: list[int] = [3, 4, 5, 6]
    x: int = 0
    y: int = 3
    assert sub(b, x, y) == [3, 4, 5]


def test_sub_edge() -> None:
    """Checks to see that an empty list returns an empty list."""
    b: list[int] = []
    x: int = 1
    y: int = 5
    assert sub(b, x, y) == []


def test_add_at_index_mutate() -> None:
    """Checks to see that the inputted list was mutated."""
    c: list[int] = [1, 3, 4]
    a: int = 2
    b: int = 1
    add_at_index(c, a, b)
    assert c == [1, 2, 3, 4]


def test_add_at_index_values() -> None:
    """Checks to see that the function doesn't return a value or None."""
    c: list[int] = [7, 8, 9]
    a: int = 6
    b: int = 0
    assert add_at_index(c, a, b) == None


def test_add_at_index_edge() -> None:
    """Checks to see that the function displays an index error given the specified index is out of bounds"""
    c: list[int] = [3, 4, 6]
    a: int = 5
    b: int = 4
    with pytest.raises(IndexError):
        add_at_index(c, a, b)
