"""Produce Pascal's triangle rows using combinatorics."""

from math import comb
from typing import Iterable


def pascals_triangle(rows: int) -> Iterable[list[int]]:
    """Yield ``rows`` of Pascal's triangle."""
    for row in range(rows):
        yield [comb(row, column) for column in range(row + 1)]


if __name__ == "__main__":
    for row in pascals_triangle(6):
        print(" ".join(f"{value:3d}" for value in row))
