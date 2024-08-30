"""Help planning your tea party!"""

__author__: str = "730801797"


def main_planner(guests: int) -> None:
    """Displays the information needed to plan a tea party depending on the amount of guest."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(("Tea Bags: ") + str(tea_bags(guests)))
    print(("Treats: ") + str(treats(guests)))
    print(("Cost: $") + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed per guest."""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed per guest based on tea bags."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats."""
    return (tea_count) * 0.5 + (treat_count) * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
