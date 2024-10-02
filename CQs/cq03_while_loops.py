"""Practice with a while loop iterating over a string."""

__author__ = "730801797"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char[0] == phrase[index]:
            count = count + 1
        index = index + 1
    return count
