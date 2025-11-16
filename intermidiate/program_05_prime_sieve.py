"""List primes with the Sieve of Eratosthenes."""

from math import isqrt


def sieve(limit: int) -> list[int]:
    """Return a list of primes up to ``limit`` inclusive."""
    if limit < 2:
        return []
    is_composite = [False] * (limit + 1)
    for candidate in range(2, isqrt(limit) + 1):
        if not is_composite[candidate]:
            step = candidate
            start = candidate * candidate
            is_composite[start : limit + 1 : step] = [True] * len(
                range(start, limit + 1, step)
            )
    return [number for number in range(2, limit + 1) if not is_composite[number]]


if __name__ == "__main__":
    print(sieve(100))
