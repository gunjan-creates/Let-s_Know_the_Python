"""Compute factorial values iteratively for non-negative integers."""


def factorial(number: int) -> int:
    """Return factorial of ``number`` using an iterative loop."""
    if number < 0:
        raise ValueError("Factorial is undefined for negative integers")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


if __name__ == "__main__":
    for candidate in range(6):
        print(f"{candidate}! = {factorial(candidate)}")
