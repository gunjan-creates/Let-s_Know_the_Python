"""Explore itertools combinations and permutations."""

from itertools import combinations, permutations


def flavor_pairings(flavors: list[str]) -> list[tuple[str, str]]:
    """Return all unique flavor pairings."""
    return list(combinations(flavors, 2))


def seating_arrangements(guests: list[str]) -> list[tuple[str, ...]]:
    """Return all possible seating orders for the guests."""
    return list(permutations(guests))


if __name__ == "__main__":
    flavors = ["vanilla", "chocolate", "strawberry"]
    print(flavor_pairings(flavors))
    print(seating_arrangements(["Alice", "Bob", "Cara"]))
