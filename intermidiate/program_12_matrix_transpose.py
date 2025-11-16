"""Transpose a matrix represented as nested lists."""

from typing import Iterable

Matrix = list[list[int]]


def transpose(matrix: Matrix) -> Matrix:
    """Return the transpose of ``matrix``."""
    if not matrix:
        return []
    column_count = len(matrix[0])
    if any(len(row) != column_count for row in matrix):
        raise ValueError("All rows in the matrix must have the same length")
    return [list(column) for column in zip(*matrix)]


if __name__ == "__main__":
    sample = [[1, 2, 3], [4, 5, 6]]
    print(transpose(sample))
