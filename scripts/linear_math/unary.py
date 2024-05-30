import math

from .spec import VectorDict


def angle(a: VectorDict) -> float:
    """
    Calculate the angle of vector a with respect to the x-axis.

    :param a: The vector to calculate the angle of.
    :return: The angle of the vector in radians.
    """
    return math.atan2(a["y"], a["x"])


def magnitude(a: VectorDict) -> float:
    """
    Calculate the magnitude of vector a.

    :param a: The vector to calculate the magnitude of.
    :return: The magnitude of the vector.
    """
    return math.sqrt(a["x"] ** 2 + a["y"] ** 2)


def normalize(a: VectorDict) -> VectorDict:
    """
    Normalize vector a.

    :param a: The vector to normalize.
    :return: The normalized vector.
    :raises ValueError: If the vector is a zero vector.
    """
    mag = magnitude(a)
    if mag == 0:
        raise ValueError("Cannot normalize a zero vector")

    return {"x": a["x"] / mag, "y": a["y"] / mag}
