"""Determine whether two phrases are anagrams of each other."""

from collections import Counter
import re


def normalize(text: str) -> str:
    """Return lowercase alphanumeric characters sorted alphabetically."""
    letters = re.findall(r"[A-Za-z0-9]", text.lower())
    return "".join(sorted(letters))


def are_anagrams(left: str, right: str) -> bool:
    """Check if ``left`` and ``right`` contain the same characters."""
    return Counter(normalize(left)) == Counter(normalize(right))


if __name__ == "__main__":
    pairs = [
        ("listen", "silent"),
        ("The eyes", "They see"),
        ("Python", "typhon"),
        ("Triangle", "Integral"),
    ]
    for left, right in pairs:
        print(f"{left!r} vs {right!r} -> {are_anagrams(left, right)}")
