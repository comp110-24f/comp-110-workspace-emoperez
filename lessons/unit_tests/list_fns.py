"""Writing Functions."""

__author__ = "730801797"


def get_first(x: list[str]) -> str:
    """Return first element."""
    return x[0]


def remove_first(y: list[str]) -> None:
    """Remove first element from list y."""
    y.pop(0)


def get_and_remove_first(z: list[str]) -> str:
    """Remove and return first element."""
    result: str = z[0]
    z.pop(0)
    return result
