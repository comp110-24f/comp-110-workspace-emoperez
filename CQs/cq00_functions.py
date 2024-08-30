"""Practice with functions."""

__author__ = "730801797"


def mimic(message: str) -> str:
    """Copies the typed message."""
    return message


def main() -> None:
    """Prints the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
