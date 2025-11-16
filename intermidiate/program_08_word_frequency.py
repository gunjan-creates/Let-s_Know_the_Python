"""Count word frequencies in a block of text."""

from collections import Counter
import re
from typing import Iterable


WORD_PATTERN = re.compile(r"[A-Za-z']+")


def tokenize(text: str) -> Iterable[str]:
    """Yield lowercase words from ``text``."""
    for match in WORD_PATTERN.finditer(text.lower()):
        yield match.group()


def word_frequencies(text: str) -> Counter[str]:
    """Return a frequency counter for words in ``text``."""
    return Counter(tokenize(text))


if __name__ == "__main__":
    sample = """Python is fun. Python is powerful. Python is readable."""
    for word, count in word_frequencies(sample).most_common():
        print(f"{word:>8s} : {count}")
