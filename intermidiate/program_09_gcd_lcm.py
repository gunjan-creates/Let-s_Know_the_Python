"""Compute the greatest common divisor and least common multiple."""

from math import gcd


def lcm(left: int, right: int) -> int:
    """Return least common multiple of two integers."""
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd(left, right)


if __name__ == "__main__":
    numbers = [(21, 6), (12, 18), (7, 5)]
    for left, right in numbers:
        print(
            f"inputs=({left}, {right}) gcd={gcd(left, right)} lcm={lcm(left, right)}"
        )
