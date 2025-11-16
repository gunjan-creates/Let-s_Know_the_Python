"""Identify Armstrong (narcissistic) numbers within a range."""


def is_armstrong(number: int) -> bool:
    """Return True if ``number`` equals the sum of its powered digits."""
    digits = [int(digit) for digit in str(abs(number))]
    power = len(digits)
    return number == sum(digit**power for digit in digits)


if __name__ == "__main__":
    print([candidate for candidate in range(1, 1000) if is_armstrong(candidate)])
