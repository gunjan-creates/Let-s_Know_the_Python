"""Demonstrate advanced iterable unpacking patterns."""

from typing import Iterable, Tuple


def head_tail(values: Iterable[int]) -> Tuple[int, list[int]]:
    """Return the first element and a list of remaining elements."""
    first, *rest = values
    return first, list(rest)


def sandwich(values: Iterable[int]) -> Tuple[list[int], int, list[int]]:
    """Return head elements, a middle element, and tail elements."""
    *start, middle, end = values
    return list(start), middle, [end]


if __name__ == "__main__":
    print(head_tail([1, 2, 3, 4]))
    print(sandwich([10, 20, 30, 40, 50]))
