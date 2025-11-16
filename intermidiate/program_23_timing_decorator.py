"""Measure function execution time with a decorator."""

from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def timed(func: F) -> F:
    """Return a wrapped function that prints execution duration."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            print(f"{func.__name__} took {elapsed:.6f}s")

    return wrapper  # type: ignore[return-value]


@timed
def slow_operation(limit: int) -> int:
    """Simulate a slow computation by summing a range."""
    return sum(range(limit))


if __name__ == "__main__":
    slow_operation(1_000_000)
