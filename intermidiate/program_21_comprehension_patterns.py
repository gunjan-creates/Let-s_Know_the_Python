"""Illustrate list, set, and dictionary comprehensions."""


def comprehension_examples(values: list[int]) -> dict[str, object]:
    """Return multiple comprehension results from ``values``."""
    squares = [value * value for value in values]
    evens = {value for value in values if value % 2 == 0}
    parity = {value: ("even" if value % 2 == 0 else "odd") for value in values}
    return {"squares": squares, "evens": evens, "parity": parity}


if __name__ == "__main__":
    print(comprehension_examples(list(range(1, 11))))
