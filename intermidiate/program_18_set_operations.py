"""Showcase common set operations in Python."""


def describe_sets(left: set[str], right: set[str]) -> dict[str, set[str]]:
    """Return a dictionary with basic set operation results."""
    return {
        "union": left | right,
        "intersection": left & right,
        "difference": left - right,
        "symmetric_difference": left ^ right,
    }


if __name__ == "__main__":
    python_skills = {"loops", "functions", "classes", "typing"}
    data_skills = {"statistics", "pandas", "functions", "loops"}
    for name, result in describe_sets(python_skills, data_skills).items():
        print(f"{name:>20s}: {sorted(result)}")
