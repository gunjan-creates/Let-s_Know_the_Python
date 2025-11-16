"""Locate items in a sorted sequence using binary search."""

from typing import Sequence


def binary_search(items: Sequence[int], target: int) -> int:
    """Return the index of ``target`` in ``items`` or -1 if absent."""
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    data = [2, 4, 6, 8, 10, 12]
    print(binary_search(data, 8))
    print(binary_search(data, 5))
