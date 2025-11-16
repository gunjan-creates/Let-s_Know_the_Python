"""Identify palindromic strings while ignoring punctuation and case."""

import re


CLEAN_PATTERN = re.compile(r"[A-Za-z0-9]")


def is_palindrome(text: str) -> bool:
    """Return True if ``text`` reads the same forward and backward."""
    cleaned = "".join(CLEAN_PATTERN.findall(text)).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    samples = [
        "Madam, I'm Adam",
        "Able was I ere I saw Elba",
        "Python is fun",
    ]
    for phrase in samples:
        print(f"{phrase!r} -> {is_palindrome(phrase)}")
