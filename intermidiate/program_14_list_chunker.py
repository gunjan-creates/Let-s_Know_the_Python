"""Chunk an iterable into fixed-size blocks."""

from collections.abc import Iterable, Iterator
from itertools import islice
from typing import TypeVar

T = TypeVar("T")


def chunked(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """Yield lists of length ``size`` from ``iterable``."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    iterator = iter(iterable)
    while batch := list(islice(iterator, size)):
        yield batch


if __name__ == "__main__":
    print(list(chunked(range(10), 3)))
