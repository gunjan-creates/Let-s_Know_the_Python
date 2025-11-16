"""Sort numbers using the merge sort algorithm."""

from typing import List


def merge_sort(values: List[int]) -> List[int]:
    """Return a sorted copy of ``values`` using merge sort."""
    if len(values) <= 1:
        return values.copy()
    midpoint = len(values) // 2
    left_sorted = merge_sort(values[:midpoint])
    right_sorted = merge_sort(values[midpoint:])
    return merge(left_sorted, right_sorted)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into one sorted list."""
    merged: List[int] = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(sample))
