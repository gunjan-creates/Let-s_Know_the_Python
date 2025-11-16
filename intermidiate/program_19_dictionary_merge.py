"""Merge dictionaries with unpacking and handle overlapping keys."""

from collections.abc import Mapping


def merge_dictionaries(*mappings: Mapping[str, int]) -> dict[str, int]:
    """Merge multiple mappings, preferring values from later mappings."""
    merged: dict[str, int] = {}
    for mapping in mappings:
        merged |= mapping
    return merged


if __name__ == "__main__":
    base = {"math": 85, "science": 90}
    updated = {"science": 93, "english": 88}
    print(merge_dictionaries(base, updated))
