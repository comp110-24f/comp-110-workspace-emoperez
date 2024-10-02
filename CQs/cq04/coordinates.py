"""Coordinates program for CQ04!"""

__author__ = "730801797"


def get_coords(xs: str, ys: str) -> None:
    xs_index: int = 0
    ys_idx: int = 0
    while xs_index < len(xs):
        ys_idx = 0
        while ys_idx < len(ys):
            print("(" + xs[xs_index] + "," + ys[ys_idx] + ")")
            ys_idx += 1
        xs_index += 1
