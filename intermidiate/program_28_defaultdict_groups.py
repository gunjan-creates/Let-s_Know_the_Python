"""Group values using collections.defaultdict."""

from collections import defaultdict
from typing import Iterable


def group_by_length(words: Iterable[str]) -> dict[int, list[str]]:
    """Group words by their length and return a regular dictionary."""
    groups: defaultdict[int, list[str]] = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


if __name__ == "__main__":
    sample = ["apple", "bat", "bar", "atom", "python"]
    print(group_by_length(sample))
