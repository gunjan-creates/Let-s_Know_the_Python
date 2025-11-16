"""Create a custom context manager for temporary files."""

import os
import tempfile
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def temporary_file(suffix: str = "", prefix: str = "tmp") -> Iterator[str]:
    """Yield a temporary file path and remove it afterwards."""
    fd, path = tempfile.mkstemp(suffix=suffix, prefix=prefix)
    os.close(fd)
    try:
        yield path
    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    with temporary_file(suffix=".txt") as temp_path:
        print(f"Temporary file created at {temp_path}")
        with open(temp_path, "w", encoding="utf-8") as handle:
            handle.write("Hello from a temporary file!\n")
    print("Temporary file cleaned up.")
