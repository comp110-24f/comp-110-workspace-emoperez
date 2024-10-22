"""Working with lists!"""

__author__ = "730801797"


def all(int_list: list[int], num: int) -> bool:
    """Checks to see if num is equal to all items in the list."""
    # Result starts off as True.
    result: bool = True
    # Index is declared to traverse through int_list.
    index: int = 0
    # If a list a empty then the function is False since num won't have any values to compare it to.
    if len(int_list) < 1:
        result = False
    # The while loop traverses through the int_list and makes the result false if there is a value that doesn't equal num.
    while index < len(int_list):
        if int_list[index] != num:
            result = False
        index += 1
    # Returns the result which is either True or False.
    return result


def max(input: list[int]) -> int:
    """Finds the highest value in a list of integers."""
    # If the list is empty then a value error will be displayed.
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # Index varible is used to traverse the input list.
    index: int = 0
    # The max-num holds the highest value.
    max_num: int = input[index]
    # The while loop traverses the list by each index and compares it to the index before to see which value is greater.
    while index < len(input):
        # If the input value at the current is greater then the value of max_num is changed to that value.
        if max_num <= input[index]:
            max_num = input[index]
        index += 1
    # The max_num is returned which is the greatest value.
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks to see if two list are equal."""
    index: int = 0
    # Starts off as True until proven False.
    result: bool = True
    # Checks to see if the length of the two list are equal before running the while loop.
    if len(list_1) == len(list_2):
        # The while loop compares each index and if one of them doen't equal then the result is changed to false.
        while index < len(list_1):
            if list_1[index] != list_2[index]:
                result = False
            index += 1
    # If the length of the two list don't match then the result changes to false.
    if len(list_1) != len(list_2):
        result = False
    # Returns either True or False.
    return result


def extend(x: list[int], y: list[int]) -> None:
    """Appends the values of a second list to the first list."""
    index: int = 0
    # The while loop runs for the entire length of the second list.
    while index < len(y):
        # The value at the y index is added to the list.
        x.append(y[index])
        index += 1
