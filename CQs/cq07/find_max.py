"""Finding and removing the max."""

__author__ = "730801797"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    i: int = 0
    max: int = input[i]
    while i < len(input):
        if max <= input[i]:
            max = input[i]
        i += 1
    i = 0
    while i < len(input):
        if max == input[i]:
            input.pop(i)
        else:
            i += 1
    return max
