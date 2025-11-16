"""Generate Fibonacci numbers using a simple generator."""

from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    """Yield Fibonacci numbers indefinitely."""
    previous, current = 0, 1
    while True:
        yield previous
        previous, current = current, previous + current


if __name__ == "__main__":
    sequence = fibonacci()
    for _ in range(10):
        print(next(sequence))
