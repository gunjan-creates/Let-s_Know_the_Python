"""Build a simple data processing pipeline with generators."""

from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T", bound=int)


def square(numbers: Iterable[T]) -> Iterator[T]:
    """Yield squared numbers lazily."""
    for number in numbers:
        yield number * number  # lazy transformation avoids storing intermediate results


def filter_even(numbers: Iterable[T]) -> Iterator[T]:
    """Yield only even numbers from ``numbers``."""
    for number in numbers:
        if number % 2 == 0:
            yield number


if __name__ == "__main__":
    source = range(10)
    pipeline = filter_even(square(source))
    print(list(pipeline))
