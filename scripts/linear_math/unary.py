import math

from .spec import VectorDict


def angle(vector: VectorDict) -> float:
    """
    Calculate the angle of a vector with respect to the x-axis.

    :param vector: The vector to calculate the angle of.
    :return: The angle of the vector in radians.
    """
    return math.atan2(vector["y"], vector["x"])


def magnitude(vector: VectorDict) -> float:
    """
    Calculate the magnitude of a vector.

    :param vector: The vector to calculate the magnitude of.
    :return: The magnitude of the vector.
    """
    return math.sqrt(vector["x"] ** 2 + vector["y"] ** 2)


def normalize(vector: VectorDict) -> VectorDict:
    """
    Normalize a vector.

    :param vector: The vector to normalize.
    :return: The normalized vector.
    :raises ValueError: If the vector is a zero vector.
    """
    mag = magnitude(vector)
    if mag == 0:
        raise ValueError("Cannot normalize a zero vector")

    return {"x": vector["x"] / mag, "y": vector["y"] / mag}
