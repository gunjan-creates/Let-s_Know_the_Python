"""Check whether numbers are prime using trial division."""

import math


def is_prime(number: int) -> bool:
    """Return True when ``number`` is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    limit = int(math.isqrt(number))
    for factor in range(5, limit + 1, 6):
        if number % factor == 0 or number % (factor + 2) == 0:
            return False
    return True


if __name__ == "__main__":
    for value in range(1, 21):
        marker = "prime" if is_prime(value) else "composite"
        print(f"{value:2d} -> {marker}")
