"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730801797"


def input_word() -> str:
    """Checks the inputted word for length. If it doesn't equal 5 then error message is printed."""
    """Will exit run if the length of user_guess isn't 5."""
    user_guess: str = input("Enter a 5-character word: ")
    if len(user_guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_guess


def input_letter() -> str:
    """Checks the inputted letter for length. If it doesn't equal 1 then error message is printed."""
    """Will exit run if the length of user_letter isn't 1."""
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:
        print("Error: Charcter must be a single character.")
        exit()
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """Runs only if the word and letter variable are the correct lenght."""
    """Searches through each index of the word to see where it matches with the letter."""
    """If it does match then it adds to the count of instances and prints out a message at where each instance was found."""
    print("Searching for " + letter + " in " + word)
    instances: int = int(0)
    if len(word) == 5 and len(letter) == 1:
        if word[0] == letter[0]:
            instances = int(instances + 1)
            print(letter + " found at index 0")
        if word[1] == letter[0]:
            instances = int(instances + 1)
            print(letter + " found at index 1")
        if word[2] == letter[0]:
            instances = int(instances + 1)
            print(letter + " found at index 2")
        if word[3] == letter[0]:
            instances = int(instances + 1)
            print(letter + " found at index 3")
        if word[4] == letter[0]:
            instances = int(instances + 1)
            print(letter + " found at index 4")
    print(str(instances) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Makes a call to the contains_char function which then calls the other two functions, input_word and input_letter."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
