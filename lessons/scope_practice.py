"""Some scope examples."""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed"""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if not (msg[index] == char):  # if msg[index] != char
            copy += msg[index]  # copy = copy + msg[index]
        index += 1  # index = index + 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # GLOBAL variable
    print(remove_chars(msg=word, char="y"))  # with keyword arguements
    # print the result of calling your function with arguemetns word and "o"


def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(idx)
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)
