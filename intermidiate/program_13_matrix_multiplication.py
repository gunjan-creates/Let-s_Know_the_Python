"""Multiply two matrices using list comprehensions."""

from typing import Sequence

Matrix = Sequence[Sequence[float]]


def multiply(left: Matrix, right: Matrix) -> list[list[float]]:
    """Return the matrix product of ``left`` and ``right``."""
    if not left or not right:
        raise ValueError("Both matrices must be non-empty")
    left_columns = len(left[0])
    right_rows = len(right)
    if left_columns != right_rows:
        raise ValueError("Incompatible dimensions for multiplication")
    if any(len(row) != left_columns for row in left):
        raise ValueError("Left matrix rows must share the same length")
    if any(len(row) != len(right[0]) for row in right):
        raise ValueError("Right matrix rows must share the same length")
    right_transposed = list(zip(*right))
    return [
        [sum(a * b for a, b in zip(left_row, right_column)) for right_column in right_transposed]
        for left_row in left
    ]


if __name__ == "__main__":
    first = [[1, 2], [3, 4], [5, 6]]
    second = [[7, 8, 9], [10, 11, 12]]
    print(multiply(first, second))
