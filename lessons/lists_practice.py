"""Basic syntax of lists."""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# print(my_numbers)

# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)

# print(my_numbers)

# my_name: str = ""  # literal
# my_name: str = str()  # constructor

# Creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# Modifying by Index
game_points[1] = 72
print(game_points)

# (Because lists are mutable)
# class_num: str = "110"  # change it to "210"
# class_num[0] = "2"

# Getting the Length
(len(game_points))

# Removing an item
game_points.pop(1)
print(game_points)

# Function name: display
# Parameter: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points


def display(nums: list[int]):
    idx: int = 0
    while idx < len(nums):
        print(nums[idx])
        idx += 1


print(display(game_points))
