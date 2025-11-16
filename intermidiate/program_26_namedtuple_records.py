"""Store lightweight records with namedtuple."""

from collections import namedtuple

Point = namedtuple("Point", "x y z")


def distance(point: Point) -> float:
    """Return the Euclidean distance of ``point`` from the origin."""
    return (point.x**2 + point.y**2 + point.z**2) ** 0.5


if __name__ == "__main__":
    sample = Point(3, 4, 12)
    print(sample)
    print(distance(sample))
