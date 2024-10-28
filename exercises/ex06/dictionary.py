"""Function work with dictionaries!"""

__author__ = "730801797"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values, raising a KeyError if duplicates exist."""
    new_dict: dict[str, str] = (
        {}
    )  # Establishes a blank dictionary to hold inverted pairs
    for key in input:  # Traverse each key in the input dictionary
        value = input[key]  # Assign the current value of input at key to variable
        if value in new_dict:  # If the value already exists as a key in new_dict
            raise KeyError(
                "Matching keys not allowed!"
            )  # Raise an error for duplicates
        new_dict[value] = key  # Assign the inverted pair in new_dict
    return new_dict  # Return the new dictionary with inverted key-value pairs


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the color with the highest count in the favorites dictionary."""
    colors_list: list[str] = []  # Creates an empty list to hold favorite colors
    for color in favorites.values():  # Collect each color in favorites
        colors_list.append(color)  # Add each color to colors_list
    color_counts = count(
        colors_list
    )  # Call count function to get occurrences of colors
    max_color = ""  # Holds the color with the highest count
    max_count = 0  # Holds the highest count value of any color
    for color in color_counts:  # Traverse each color in the count dictionary
        if (
            color_counts[color] > max_count
        ):  # If the count of color is greater than max_count
            max_color = color  # Update max_color to the current color
            max_count = color_counts[color]  # Update max_count to the new highest count
    return max_color  # Return the color with the highest count


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of occurrences of each value in a list."""
    result: dict[str, int] = {}  # Empty dictionary to hold value and its count
    for value in values:  # Traverse each value in the list
        if value in result:  # If the value is already a key in result
            result[value] += 1  # Increment the count for that value by 1
        else:  # If the value is not in result
            result[value] = 1  # Add the value with an initial count of 1
    return result  # Return the result dictionary containing counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Sorts a list of words into a dict of letter keys and word values."""
    result: dict[str, list[str]] = (
        {}
    )  # Creates a dict with key str, and the values of a list
    for word in words:  # Traverse the list of words
        letter = word[0].lower()  # Get the first letter, lowercased
        # If the letter is not already a key in result, initialize it with an empty list
        if letter not in result:
            result[letter] = []
        # Append the word to the list of the corresponding letter
        result[letter].append(word)
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance dictionary with a new student for a specific day."""
    if day in attendance:  # Checks if the day already exists in the dictionary
        if (
            student not in attendance[day]
        ):  # Checks if the student is not already in the list for that day
            attendance[day].append(student)  # Adds the student to the list for that day
    else:
        attendance[day] = [
            student
        ]  # Creates a new entry for the day with the student as the only item in the list
    return None  # Returns None, as the dictionary is mutated directly


#  from exercises.ex06.dictionary import invert
#  from exercises.ex06.dictionary import favorite_color
#  from exercises.ex06.dictionary import count
#  from exercises.ex06.dictionary import alphabetizer
#  from exercises.ex06.dictionary import update_attendance
