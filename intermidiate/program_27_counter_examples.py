"""Use collections.Counter to find most common elements."""

from collections import Counter


def most_common_letters(text: str, count: int = 3) -> list[tuple[str, int]]:
    """Return the ``count`` most common letters in ``text``."""
    filtered = [character.lower() for character in text if character.isalpha()]
    return Counter(filtered).most_common(count)


if __name__ == "__main__":
    sample = "Mississippi River"
    print(most_common_letters(sample))
