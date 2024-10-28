"""Implementing list utility functions."""

__author__ = "730801797"


def only_evens(nums: list[int]) -> list[int]:
    """Makes a list with only the even values of the inputted list"""
    i: int = 0  # Index at zero to traverse at the start of the list.
    result: list[int] = []  # New empty list is created to store the even values.
    while i < len(nums):  # While loop traverses through the list indexes.
        if (
            nums[i] % 2 == 0
        ):  # The MOD operator is used to check if a number is even if its remainder is zero after dividing by 2.
            result.append(
                nums[i]
            )  # If the function is run then the value at the index is added the result list.
        i += 1  # One is added to the index to countinue traversing through the list.
    return result  # The return value is the result list.


def sub(digits: list[int], x: int, y: int) -> list[int]:
    """Makes a list with the values within a specified range."""
    i: int = x  # Index starts at the value of x because its the start of the new list.
    result: list[int] = (
        []
    )  # New empty list is created to store the values within the range.
    if x < 0:  # If the start of the range is a negative number
        i = 0  # Then the list will begin at the start of the list at index 0.
    if y > len(digits):  # If the end of the range exceeds the length of the range
        y = len(digits)  # Then the list will end at the length of the list.
    if (
        len(digits) == 0 or x >= len(digits) or y == 0
    ):  # If the list is empty or the start of the range exceeds the lenght of the list or if the end of the list starts at the begginng of the list
        return result  # Then the return value is an empty list.
    while (
        i < y
    ):  # While i is less then y the value at the index is appended to the result list.
        result.append(digits[i])
        i += 1  # One is added to i to countinue traversing through the list.
    return result  # The return value is the result list.


def add_at_index(input: list[int], a: int, b: int) -> None:
    """Adds a value at the speciefied index."""
    input.append(0)  # The value 0 is appended to create an index for the value.
    i: int = (
        len(input) - 2
    )  # The index is the length of the input list minus two so it can appropraitely shift the values.
    if (
        b < 0 or b > len(input) - 1
    ):  # If the index is less tha 0 or exceeds the length of the list or the list is empty
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # Then an index error is displayed.
    while i >= b:  # While the index is less than or equal to the desired index...
        input[i + 1] = input[
            i
        ]  # the input list index +1 is equal to the input list index.
        i = i - 1  # The index is equal to index -1 to move to the left of the list.
    input[b] = a  # The input list index at value b is equalled to the value of a.
