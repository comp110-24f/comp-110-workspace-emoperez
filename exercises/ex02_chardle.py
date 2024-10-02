"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730801797"


def input_word() -> str:
    """Checks the inputted word for length. If it doesn't equal 5 then error message is printed."""
    """Will exit run if the length of user_guess isn't 5."""
    user_guess: str = input("Enter a 5-character word: ")
    if len(user_guess) != 5:
        # If the length of the user_guess is not 5 the print command will run followed by exiting the program.
        print("Error: Word must contain 5 characters.")
        exit()
    # Otherwise the length of user_guess equals 5 and the program countinues and returns what the user inputted.
    return user_guess


def input_letter() -> str:
    """Checks the inputted letter for length. If it doesn't equal 1 then error message is printed."""
    """Will exit run if the length of user_letter isn't 1."""
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:
        # If the length of the user_letter is not 1 the print command will run followed by exiting the program.
        print("Error: Character must be a single character.")
        exit()
    # Otherwise the length of input_letter equals 1 and the program countinues and returns what the user inputted.
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """Runs only if the word and letter variable are the correct lenght."""
    """Searches through each index of the word to see where it matches with the letter."""
    """If it does match then it adds to the count of instances and prints out a message at where each instance was found."""
    print("Searching for " + letter + " in " + word)
    # The instances variabels is used for the wording output by the print function in regard to "instance(s)".
    # The count is used to detteremine the amount of times a letter was found and gets 1 added each time and if statement is run.
    instances: str = str("No instances")
    count: int = int(0)
    # The length of word has to equal 5 and length of letter has to equal 1 for program to run within the if function.
    if len(word) == 5 and len(letter) == 1:
        # Here the word is compared at every index, up to 4, by the letter index 0 to see if the characters match.
        if word[0] == letter[0]:
            # If the statement is true  the count goes up by one and the letter along with where it was found is printed.
            count = count + 1
            print(letter + " found at index 0")
        if word[1] == letter[0]:
            count = count + 1
            print(letter + " found at index 1")
        if word[2] == letter[0]:
            count = count + 1
            print(letter + " found at index 2")
        if word[3] == letter[0]:
            count = count + 1
            print(letter + " found at index 3")
        if word[4] == letter[0]:
            count = count + 1
            print(letter + " found at index 4")
        # The conditionals will check if the count is greater than 1, equal to 1, or 0 then it'll change the instances string value.
        if count > 1:
            # If count is greater than 1 the varible instances changes to a string with the count concatenated with "instances".
            instances = str(str(count) + " instances")
        elif count == 1:
            # If count is equal to 1 the varible instances changes to a string with the count concatenated with "instance".
            instances = str(str(count) + " instance")
        else:
            # If count is 0 the varible instances changes to a string with "No instances".
            instances = str("No instances")
    # Here print is run which outputs a string that says the amount of instances the letter was found in the word.
    print(instances + " of " + letter + " found in " + word)


def main() -> None:
    """Makes a call to the contains_char function which then calls the other two functions, input_word and input_letter."""
    contains_char(word=input_word(), letter=input_letter())


# Makes a call to the main function which runs the program.
if __name__ == "__main__":
    main()
