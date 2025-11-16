"""Demonstrate a recursive factorial implementation."""

from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(number: int) -> int:
    """Compute factorial recursively with memoization for efficiency."""
    if number < 0:
        raise ValueError("Factorial is undefined for negative integers")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    print(f"10! = {factorial(10)}")
