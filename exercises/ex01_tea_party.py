"""Help planning your tea party!"""

__author__: str = "730801797"


def main_planner(guests: int) -> None:
    """Displays the information needed to plan a tea party depending on the amount of guests."""
    # Prints the amount of guests attending in a string by concatenating the different strings.
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Prints the number of tea bags needed in a string.
    print(("Tea Bags: ") + str(tea_bags(guests)))
    # Prints the number of treats needed in a string.
    print(("Treats: ") + str(treats(guests)))
    # Prints the total cost, in regard to the number of tea bags and treats, in a string.
    print(("Cost: $") + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed per guest."""
    # Multiplies the amount of people by 2 to get the number of tea bags needed.
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed per guest based on tea bags."""
    # Multiplies the amount of people, taken from the tea_bags function, by 1.5 and makes it into a integer.
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats."""
    # Adds the products of (tea_count * 0.5) and (treat_count * 0.75) to get the cost which returns a float.
    return (tea_count) * 0.5 + (treat_count) * 0.75


if __name__ == "__main__":
    # Makes a call to the main planner function and runs the program after taking the input of number of guests.
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
