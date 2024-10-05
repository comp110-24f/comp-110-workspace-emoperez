"""Mutating functions."""

__author__ = "730801797"


def manual_append(x: list[int], y: int) -> None:
    x.append(y)


def double(y: list[int]) -> None:
    index: int = 0
    while index < len(y):
        y[index] = y[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


double(list_2)

print(list_1)
print(list_2)
