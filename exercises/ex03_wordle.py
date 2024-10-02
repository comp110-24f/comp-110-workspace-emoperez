"""One word. Five letters. Six guesses. Play Wordle!"""

__author__ = "730801797"


def input_guess(secret_word_len: int) -> str:
    """Checks to see if the word guess is the appropriate length."""
    # The varible input_guess is created to prompt the user to type in a guess.
    # The input uses a fstring so the secret_word_len varible is automatically transformed to a string.
    input_guess: str = input(f"Enter a {secret_word_len} character word: ")
    # The while loop runs if a word isn't the length of the secret word.
    while len(input_guess) != secret_word_len:
        # When the while loop runs it ask again for the input_guess and equals it to the new guess.
        input_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    # If the while loop doesn't run then it returns the input_guess.
    return input_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks to see if a character is contained in the secret word."""
    # The assert command lets us know the length of char_guess has to be 1.
    assert len(char_guess) == 1
    # index is declared for while loop to traverse every index.
    index: int = 0
    # The varible result is used to keep track of the return value and is false unless it's changed to true.
    result: bool = False
    # The while loop goes through every index of the secret word and checks if char_guess is equal to it at every index.
    while index < len(secret_word):
        # If it's equal at any index the result changes to true.
        if char_guess == secret_word[index]:
            result = True
        index += 1
    # The result displays a bool value and will result in False unless it was changed in the if statement to True.
    return result


def emojified(guess: str, secret: str) -> str:
    """Checks the index of each word to see if it's part of the secret word."""
    # The assert command makes sure the length of guess and secret are the smae otherwise the rest of the progrma won't run.
    assert len(guess) == len(secret)
    # The index is set to 0 so it can traverse thorugh each index of secret and guess.
    index: int = 0
    # The result varible is created to carry the emoji that corresponds for that index of guess.
    result: str = ""
    # The color boxes varibles are declared so we don't havae to rewrite the emoji code.
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # The while loop is used to traverse the indexes of guess which is establishd to be the same length as secret.
    while index < len(secret):
        # If the index of guess matches the index of secret a green box is added to the result string.
        if guess[index] == secret[index]:
            result = result + GREEN_BOX
        # If the index doesn't match then the contains_char function is called to check if it's in the secret word.
        # If it's True then a yellow box is added to the result string.
        elif (contains_char(secret, guess[index])) == True:
            result = result + YELLOW_BOX
        # If none of the previos statements are true then a white box is added to the result string.
        # The white box means the letter at the index isn't in the word at all.
        else:
            result = result + WHITE_BOX
        # The index adds one to countinue traversing through the while loop.
        index += 1
    # The return value is the string of emojis created by the while loop.
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Establish the currents turn the player is at.
    turns: int = 1
    # Displays the string that tells the player what turn they are on.
    turn_count: str = "=== Turn " + str(turns) + "/6 ==="
    print(turn_count)
    # Ask for the players guess and makes a call to the input_guess function to ensure it's the proper length.
    input_try: str = input_guess(len(secret))
    # Makes a call to the emojified function and prints it to help the player guess the word.
    print(emojified(input_try, secret))
    # The while loop takes into the amount of 6 turns allowed and runs only if there is less then 6 used.
    while turns < 6:
        # If the word input by the player matches the secret word then it displays a message letting the player know and how many tries it took them.
        if input_try == secret:
            print(f"You won in {turns}/6 turns!")
            # If the statement runs turns is equaled to a number larger then six so the while loop won't run again.
            turns = 10
        # If the word input by the player is incorrect then it'll run the same steps of turn number, taking input, and emojifying.
        elif input_try != secret:
            turn_count = "=== Turn " + str(turns + 1) + "/6 ==="
            print(turn_count)
            input_try = input_guess(len(secret))
            print(emojified(input_try, secret))
        # If the amount of turns plus 1 equal six then a print message is displayed to let the player know they failed.
        if (turns + 1) == 6:
            print("X/6 - Sorry, try again tommorrow!")
        # The turns += 1 is used to help traverse through the while loop to help determine wether it's equal, needs to run again, or turns are used up.
        turns += 1


# Makes call to main function and runs the program with the secret word being "codes".
if __name__ == "__main__":
    main(secret="codes")
