"""Implement quick sort with list comprehensions."""

from typing import List


def quick_sort(values: List[int]) -> List[int]:
    """Return a sorted copy of ``values`` using quick sort."""
    if len(values) <= 1:
        return values.copy()
    pivot = values[0]
    smaller = [value for value in values[1:] if value <= pivot]
    larger = [value for value in values[1:] if value > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)


if __name__ == "__main__":
    sample = [29, 10, 14, 37, 13]
    print(quick_sort(sample))
